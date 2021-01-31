from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('inicio/', views.inicio),
    path('home/', views.home),
    path('exams/', views.exams),
    path('meds/', views.meds),
    path('cal/', views.cal),
    path('', views.Paciente.as_view(), name='paciente'),
    path('lista/', views.ListaPacientes.as_view(), name='lista'),
    path('crear', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
]
