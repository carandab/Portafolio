from django.db import models

    
class Skill(models.Model):
    
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)  # Ingresar FontAwesome class name
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,
            choices=[
                ('frontend', 'Frontend'),
                ('backend', 'Backend'),
                ('database', 'Database'),
                ('softskill', 'Soft Skill'),
            ]
        )
    
    def __str__(self):
        return self.name

class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text='Imagen principal del proyecto')
    published_at = models.DateTimeField(auto_now_add=True)
    host_url = models.URLField(blank=True, null=True, verbose_name='URL de Demo')
    github_url = models.URLField(blank=True, null=True, verbose_name='URL de GitHub')
    
    # Campo para orden personalizado
    order = models.PositiveIntegerField(
        default=0, 
        help_text='Orden de visualización (menor número = aparece primero). Por defecto 0.'
    )

    # Relación con Skill
    skills = models.ManyToManyField(Skill, related_name='projects')
    
    class Meta:
        ordering = ['order', '-published_at']  # Ordena por 'order' primero, luego por fecha
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title




# Para carrusel de imagenes en modal de proyectos
""" class ProjectImage(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, help_text='Descripción opcional de la imagen')
    order = models.PositiveIntegerField(default=0, help_text='Orden en el carrusel (menor número = primera)')
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Imagen de Proyecto'
        verbose_name_plural = 'Imágenes de Proyecto'
    
    def __str__(self):
        return f"{self.project.title} - Imagen {self.order}" """