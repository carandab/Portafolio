from django.urls import path
from . import views

urlpatterns = [
    # Lista de proyectos
    path('', views.project_list, name="lista_proyectos"),
   
    # CRUD de proyectos (requiere autenticación)
    path('crear/', views.project_create, name="crear_proyecto"),
    path('<int:pk>/editar/', views.project_update, name="editar_proyecto"),
    path('<int:pk>/eliminar/', views.project_delete, name="eliminar_proyecto"),

    # Consulta SQL
    path('sql/', views.consulta_sql, name="consulta_sql"),
]