from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
import markdown
import os
from django.conf import settings
from .models import Project, Skill
from .forms import ProjectForm

def index(request):


    # Obtener habilidades por tipo
    frontend_skills = Skill.objects.filter(type='frontend')
    backend_skills = Skill.objects.filter(type='backend')
    database_skills = Skill.objects.filter(type='database')
    softskills = Skill.objects.filter(type='softskill')
    
    context = {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'database_skills': database_skills,
        'softskills': softskills,
    }
    
    return render(request, 'index.html', context)

# CRUD Habilidades (En desuso)

def create_skill(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        Skill.objects.create(name=name, type=type)
        return redirect("index")
    return render(request, "recursos/skill_form.html")

def update_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        skill.name = request.POST.get("name")
        skill.type = request.POST.get("type")
        skill.save()
        return redirect("index")
    return render(request, "recursos/skill_form.html", {"skill": skill})

def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        skill.delete()
        return redirect("index")
    return render(request, "recursos/skill_confirm_delete.html", {"skill": skill})

# LISTA DE PROYECTOS
def project_list(request):
    # Muestra todos los proyectos

    proyectos = Project.objects.all().prefetch_related('skills')
    return render(request, "recursos/project_list.html", {"proyectos": proyectos})

# DETALLE DE PROYECTO
def project_detail(request, pk):

    proyecto = get_object_or_404(Project, pk=pk)
    
    context = {
        'proyecto': proyecto,
    }
    
    return render(request, "recursos/project_detail.html", context)


# CREAR PROYECTO 
@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProjectForm()

    return render(request, "recursos/project_form.html", {"form": form})


# EDITAR PROYECTO
@login_required
def project_update(request, pk):
    proyecto = get_object_or_404(Project, pk=pk)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProjectForm(instance=proyecto)

    return render(request, "recursos/project_form.html", {"form": form})


# ELIMINAR PROYECTO
@login_required
def project_delete(request, pk):
    proyecto = get_object_or_404(Project, pk=pk)
    
    if request.method == "POST":
        proyecto.delete()
        return redirect("lista_proyectos")
    
    return render(request, "recursos/project_confirm_delete.html", {"object": proyecto})


# CONSULTA SQL
def consulta_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.title, s.name, s.type
            FROM recursos_project p
            JOIN recursos_project_skills ps ON p.id = ps.project_id
            JOIN recursos_skill s ON s.id = ps.skill_id
            ORDER BY p.published_at DESC;
        """)
        resultados = cursor.fetchall()
    return render(request, "recursos/sql.html", {"resultados": resultados})


# README VIEW
def readme_view(request):
    readme_path = os.path.join(settings.BASE_DIR, 'README.md')
    
    try:
        with open(readme_path, 'r', encoding='utf-8', errors='ignore') as file:
            readme_content = file.read()
        
        # Convertir Markdown a HTML permitiendo HTML dentro
        html_content = markdown.markdown(
            readme_content,
            extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.tables',
                'markdown.extensions.toc',
                'markdown.extensions.nl2br',
                'markdown.extensions.extra',  # ← Agrega esta
            ],
            extension_configs={
                'markdown.extensions.extra': {
                    'markdown_in_html': True  # ← Permite HTML
                }
            }
        )
        
    except FileNotFoundError:
        html_content = "<div class='alert alert-warning'><i class='fas fa-exclamation-triangle me-2'></i>README.md no encontrado.</div>"
    except Exception as e:
        html_content = f"<div class='alert alert-danger'><i class='fas fa-exclamation-circle me-2'></i>Error: {str(e)}</div>"
    
    context = {
        'readme_html': html_content,
    }
    
    return render(request, 'recursos/readme.html', context)