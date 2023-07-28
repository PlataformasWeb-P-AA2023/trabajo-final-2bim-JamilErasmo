
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.index1, name='index1'),
        path('index2', views.index2, name='index2'),
        path('crear/barrio', views.crear_Barrio, name = 'crear_barrio'),
        path('crear/persona', views.crear_Persona, name = 'crear_persona'),
        path('crear/local/comida', views.crear_LocalComida, name = 'crear_local_comida'),
        path('crear/local/respuestos', views.crear_LocalRespuestos, name = 'crear_local_respuestos'),
        path('editar/barrio/<int:id>', views.editar_Barrio, name = 'editar_barrio'),
        path('editar/persona/<int:id>', views.editar_Persona, name = 'editar_persona'),
        path('editar/local/comida/<int:id>', views.editar_LocalComida, name = 'editar_local_comida'),
        path('editar/local/respuestos/<int:id>', views.editar_LocalRespuestos, name = 'editar_local_respuestos'),
        path('eliminar/barrio/<int:id>', views.eliminar_Barrio, name = 'eliminar_Barrio'),
        path('eliminar/persona/<int:id>', views.eliminar_Persona, name = 'eliminar_Persona'),
        path('eliminar/local/comida/<int:id>', views.eliminar_LocalComida, name = 'eliminar_local_comida'),
        path('eliminar/local/respuestos/<int:id>', views.eliminar_LocalRespuestos, name = 'eliminar_local_respuestos'),
        
 ]