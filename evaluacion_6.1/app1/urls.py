from django.urls import path
from . import views

app_name="app1"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.home),
    path('exams/', views.exams),
    path('meds/', views.meds),
    path('cal/', views.cal),
    path('lista/', views.ListaPaciente.as_view(), name='lista'),
    path('crear/', views.CrearPaciente.as_view(), name='crear'),
    path('<int:pk>/editar', views.EditarPaciente.as_view(), name='editar'),
    path('<int:pk>/eliminar', views.EliminarPaciente.as_view(), name='eliminar'),
    path('crear_examen/', views.AgregarExamen.as_view(), name='agregar_examen'),
    path('examenes', views.ExamenesView.as_view(), name='examen'),
]
