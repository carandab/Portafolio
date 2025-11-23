from django.contrib import admin
from .models import Skill, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'icon')
    list_filter = ('type',)
    search_fields = ('name',)
    ordering = ('type', 'name')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'description')
    filter_horizontal = ('skills',)
    ordering = ('-published_at',)