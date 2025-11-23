from django import forms
from .models import Project, Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'icon', 'type']


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
            'habilidades': forms.CheckboxSelectMultiple()
        }