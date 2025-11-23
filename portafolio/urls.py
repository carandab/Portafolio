from django.contrib import admin
from django.urls import path, include
from recursos import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('proyectos/', include('recursos.urls')),
]
