from django.shortcuts import render, redirect
from .models import  Barrio, LocalRepuesto, LocalComida, Persona
from .forms import  LocalComidaForm, LocalRepuestoForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .serializers import *
from rest_framework import viewsets, permissions

# importar las clases de models.py
from app.models import *

# importar los formularios de forms.py
from app.forms import *


# Create your views here.
def index(request):
    localComida = LocalComida.objects.all()
    diccionario = {'LocalComida': localComida, 'num_localComida': len(localComida)}
    return render(request, 'index.html', diccionario)

def index2(request):
    localRepuesto = LocalRepuesto.objects.all()
    diccionario = {'LocalRepuestos': localRepuesto, 'num_localRepuesto': len(localRepuesto)}
    return render(request, 'index2.html', diccionario)

#

def crear_persona(request):
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_persona.html', diccionario)

def editar_persona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_persona.html', diccionario)

def eliminar_persona(request, id):
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)

#

def crear_barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)

def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_barrio.html', diccionario)

def eliminar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)

#

def crear_local_comida(request):
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalComidaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_local_comida.html', diccionario)

def editar_local_comida(request, id):
    localCo = LocalComida.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST, instance=localCo)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalComidaForm(instance=localCo)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_local_comida.html', diccionario)

def eliminar_local_comida(request, id):
    localCo = LocalComida.objects.get(pk=id)
    localCo.delete()
    return redirect(index)

#
#
#

def crear_local_repuestos(request):
    if request.method=='POST':
        formulario = LocalRepuestoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index2)
    else:
        formulario = LocalRepuestoForm()
    diccionario = {'formulario': formulario}
    return render(request, 'crear_local_repuestos.html', diccionario)

def editar_local_repuestos(request, id):
    localRe = LocalRepuesto.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalRepuestoForm(request.POST, instance=localRe)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index2)
    else:
        formulario = LocalRepuestoForm(instance=localRe)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_local_repuestos.html', diccionario)

def eliminar_local_repuestos(request, id):
    localRe = LocalRepuesto.objects.get(pk=id)
    localRe.delete()
    return redirect(index2)

#

def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalComidaViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalRepuestoViewSet(viewsets.ModelViewSet):
# class NumeroTelefonicoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LocalRepuesto.objects.all()
    serializer_class = LocalRepuestoSerializer
    permission_classes = [permissions.IsAuthenticated]
