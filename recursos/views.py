from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection

from .models import Project, Skill
from .forms import ProjectForm

def index(request):
    return render(request, 'index.html')

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
