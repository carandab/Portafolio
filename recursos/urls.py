from django.urls import path
from . import views
from recursos.views import project_list as lista_proyectos
from recursos.views import project_create as crear_proyecto
#from recursos.views import consulta_sql

urlpatterns = [
    path('', lista_proyectos, name="lista_proyectos"),
    #path('<int:pk>/', detalle_proyecto, name="detalle_proyecto"),
    path('crear/', crear_proyecto, name="crear_proyecto"),
    #path('sql/', consulta_sql, name="consulta_sql"),
]