from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from proyecto_app.models import *
from proyecto_app.forms import *
from .serializers import *
# Create your views here.
def index1(request):
    barrio = Barrio.objects.all()
    persona = Persona.objects.all()
    localComida = LocalComida.objects.all()
    localRepuestos = LocalRepuestos.objects.all()
    num_localComida = len(localComida)
    diccionario = {'num_localComida': num_localComida, 'localComida': localComida}
    return render(request, 'index1.html', diccionario)

#

def index2(request):
    barrio = Barrio.objects.all()
    persona = Persona.objects.all()
    localComida = LocalComida.objects.all()
    localRepuestos = LocalRepuestos.objects.all()
    num_localRespuestos = len(localRepuestos)
    diccionario = {'num_locaRespuestos': num_localRespuestos, 'localRespuestos': localRepuestos}
    return render(request, 'index2.html', diccionario)

#

def crear_Barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index1)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)

def editar_Barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index1)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_barrio.html', diccionario)

def eliminar_Barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index1)

#

def crear_Persona(request):
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index1)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_persona.html', diccionario)

def editar_Persona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index1)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_persona.html', diccionario)

def eliminar_Persona(request, id):
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index1)

#

def crear_LocalComida(request):
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index1)
    else:
        formulario = LocalComidaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_local_comida.html', diccionario)

def editar_LocalComida(request, id):
    localComida = LocalComida.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST, instance=localComida)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index1)
    else:
        formulario = LocalComidaForm(instance=localComida)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_local_comida.html', diccionario)

def eliminar_LocalComida(request, id):
    localComida = LocalComida.objects.get(pk=id)
    localComida.delete()
    return redirect(index1)

#

def crear_LocalRespuestos(request):
    if request.method=='POST':
        formulario = LocalRespuestosForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index2)
    else:
        formulario = LocalRespuestosForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_local_respuestos.html', diccionario)

def editar_LocalRespuestos(request, id):
    localRespuestos = LocalRepuestos.objects.get(pk=id)  # Cambia LocalRespuestosForm por LocalRepuestos
    if request.method == 'POST':
        formulario = LocalRespuestosForm(request.POST, instance=localRespuestos)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index2)
    else:
        formulario = LocalRespuestosForm(instance=localRespuestos)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_local_respuestos.html', diccionario)


def eliminar_LocalRespuestos(request, id):
    localRespuestos = LocalRepuestos.objects.get(pk=id)
    localRespuestos.delete()
    return redirect(index2)

#

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocalComidaViewSet(viewsets.ModelViewSet):
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalRespuestosViewSet(viewsets.ModelViewSet):
    queryset = LocalRepuestos.objects.all()
    serializer_class = LocalRepuestosSerializer
    permission_classes = [permissions.IsAuthenticated]