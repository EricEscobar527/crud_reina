from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Citas(models.Model):
    
    fecha_hora = models.DateTimeField()
    paciente = models.CharField(max_length=250)
    tiempo = models.IntegerField()
    medico = models.CharField(max_length=250)
    cita = models.IntegerField()
    estatus = models.IntegerField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.paciente
