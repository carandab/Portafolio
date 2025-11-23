from django.db import models

    
class Skill(models.Model):
    
    icon = models.CharField(max_length=100)  # Ingresar FontAwesome class name
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
    image = models.ImageField(upload_to='projects/')
    published_at = models.DateTimeField(auto_now_add=True)
    host_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True)


    skills = models.ManyToManyField(Skill, related_name='projects')
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
