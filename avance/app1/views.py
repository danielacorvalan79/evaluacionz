
from django.shortcuts import render, redirect
from .forms import RegistroPaciente, LoginForm
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.views import generic
from django.views.generic import ListView
from .models import Pacientes
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
def inicio(request):
    return render(request, 'app1/index.html')

def home(request):
    return render(request, 'app1/main.html') 

def register(request):
    return render(request, 'app1/registro.html')  

def exams(request):
    return render(request, 'app1/examenes.html') 

def meds(request):
    return render(request, 'app1/medicamento.html')

def cal(request):
    return render( request, 'app1/calendario.html')

class Paciente(generic.TemplateView):
    template_name = 'app1/home.html'

class ListaPacientes(ListView):
    model=Pacientes
    template_name = 'app1/lista_pacientes.html'
    context_object_name = 'pacientes'

class CrearPaciente(CreateView):
    model=Pacientes
    template_name = 'app1/crear_paciente.html'
    fields='__all__'
    success_url= reverse_lazy('app1:lista')


class EditarPaciente(UpdateView):
    model=Paciente
    template_name = 'app1/editar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista')


class EliminarPaciente(DeleteView):
    model=Paciente
    template_name = 'app1/eliminar_paciente.html'
    fields='__all__'
    success_url=reverse_lazy('app1:lista')
    context_object_name = 'paciente'
    