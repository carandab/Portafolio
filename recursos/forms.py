from django import forms
from .models import Project, Skill


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'image',
            'host_url',
            'github_url',
            'skills',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: GoWest Petshop',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe tu proyecto: características principales, tecnologías usadas, tu rol en el desarrollo...',
                'rows': 6,
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'host_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://tu-proyecto.onrender.com',
            }),
            'github_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/usuario/repositorio',
            }),
            'skills': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': '10',
            }),
        }
        labels = {
            'title': 'Título del Proyecto',
            'description': 'Descripción',
            'image': 'Imagen Principal',
            'host_url': 'URL de Demo',
            'github_url': 'URL de GitHub',
            'skills': 'Tecnologías',
        }
        help_texts = {
            'image': 'Sube una captura de pantalla del proyecto (recomendado: 1200x720px)',
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'icon', 'image', 'type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Python, Django, JavaScript',
            }),
            'icon': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: fab fa-python',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'type': forms.Select(attrs={
                'class': 'form-select',
            }),
        }