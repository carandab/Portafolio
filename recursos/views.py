from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection

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

# CRUD Habilidades

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
    proyectos = Project.objects.all()
    return render(request, "recursos/project_list.html", {"proyectos": proyectos})


""" # DETALLE DE PROYECTO
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Project, pk=pk)
    return render(request, "recursos/detalle.html", {"proyecto": proyecto})
 """

# CREAR PROYECTO (opcional: @login_required)
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_proyectos")
    else:
        form = ProjectForm()

    return render(request, "recursos/project_form.html", {"form": form})


# CONSULTA SQL (requisito explícito)
