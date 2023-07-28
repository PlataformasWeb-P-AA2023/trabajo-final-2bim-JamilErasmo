
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.index1, name='index1'),
        path('index2', views.index2, name='index2'),
        path('crear/barrio', views.crear_barrio, name = 'crear_barrio'),
        path('crear/persona', views.crear_persona, name = 'crear_persona'),
        path('crear/local/comida', views.crear_local_comida, name = 'crear_local_comida'),
        path('crear/local/repuestos', views.crear_local_repuestos, name = 'crear_local_repuestos'),
        path('editar/barrio/<int:id>', views.editar_barrio, name = 'editar_barrio'),
        path('editar/persona/<int:id>', views.editar_persona, name = 'editar_persona'),
        path('editar/local/comida/<int:id>', views.editar_local_comida, name = 'editar_local_comida'),
        path('editar/local/respuestos/<int:id>', views.editar_local_repuestos, name = 'editar_local_respuestos'),
        path('eliminar/barrio/<int:id>', views.eliminar_barrio, name = 'eliminar_Barrio'),
        path('eliminar/persona/<int:id>', views.eliminar_persona, name = 'eliminar_Persona'),
        path('eliminar/local/comida/<int:id>', views.eliminar_local_comida, name = 'eliminar_local_comida'),
        path('eliminar/local/respuestos/<int:id>', views.eliminar_local_repuestos, name = 'eliminar_local_respuestos'),
        
 ]


