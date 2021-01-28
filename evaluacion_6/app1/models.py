from django.db import models

# Create your models here.

class Paciente(models.Model):
    run = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    email = models.CharField(max_length=100, null=True)
    telefono = models.IntegerField()
    patologias = models.CharField(max_length=2000)

class Examen(models.Model):
    fecha = models.DateField()
    variable1 = models.IntegerField()
    variable2 = models.IntegerField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Medicamento(models.Model):
    fecha_indicacion = models.DateField()
    nombre = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    


