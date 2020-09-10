from django.db import models

# Create your models here.

class Cliente(models.Model):
    run = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length = 255)
    telefono = models.CharField(max_length = 12)
    email = models.CharField(max_length = 255)
    reserva = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.nombre

        
