from django.contrib import admin
from .models import Skill, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'icon')
    list_filter = ('type',)
    search_fields = ('name',)
    ordering = ('type', 'name')


""" class ProjectImageInline(admin.TabularInline):
    #Inline para agregar múltiples imágenes al proyecto
    model = ProjectImage
    extra = 1  # Número de formularios vacíos que se muestran
    fields = ('image', 'caption', 'order')
    ordering = ['order'] """


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'published_at', 'has_demo', 'has_github')
    list_filter = ('published_at',)
    search_fields = ('title', 'description')
    filter_horizontal = ('skills',)
    ordering = ('order', '-published_at')  # Ordena por 'order' primero
    #inlines = [ProjectImageInline]
    
    # Hacer que el campo 'order' sea editable desde la lista
    list_editable = ('order',)
    
    # Campos que se muestran en el formulario de edición
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'image')
        }),
        ('Enlaces', {
            'fields': ('host_url', 'github_url')
        }),
        ('Tecnologías', {
            'fields': ('skills',)
        }),
        ('Configuración', {
            'fields': ('order',),
            'description': 'Define el orden en que aparecen los proyectos. Menor número = aparece primero.'
        }),
    )
        
    def has_demo(self, obj):
        #Indica si el proyecto tiene demo"""
        return bool(obj.host_url)
    has_demo.boolean = True
    has_demo.short_description = 'Demo'
    
    def has_github(self, obj):
        #Indica si el proyecto tiene GitHub"""
        return bool(obj.github_url)
    has_github.boolean = True
    has_github.short_description = 'GitHub'


    
"""     def get_gallery_count(self, obj):
       #Muestra cuántas imágenes adicionales tiene el proyecto
        count = obj.gallery_images.count()
        return f"{count} imágenes" if count != 1 else f"{count} imagen"
    get_gallery_count.short_description = 'Galería' """



# Carrusel de fotos en modal de proyectos
""" @admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

    list_display = ('project', 'order', 'caption', 'image')
    list_filter = ('project',)
    search_fields = ('project__title', 'caption')
    ordering = ('project', 'order')
    list_editable = ('order',) """