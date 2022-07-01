from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    altura = models.FloatField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + " " + str(self.altura) + str(self.fecha_nacimiento)

"""
class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()
"""
