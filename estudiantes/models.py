from django.db import models
class Estudiante(models.Model):
    Carnet=models.CharField (max_length=20, unique=True)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField (max_length=50)
    CUI=models.CharField (max_length=13, unique= True)
    Telefono=models.CharField (max_length=15)
    Correo=models.EmailField(unique = True)
    Genero=models.CharField (max_length=10, choices= [('M','Masculino'),('F','Femenino')])
    Estado_Civil = models.CharField(max_length=10, choices=[('s', 'Soltero'), ('c', 'Casado')])
    Fecha_de_Nacimiento= models.DateField()
    
    def __str__(self):
        return f"{self.Carnet} - {self.first_name},{self.last_name}"
    
# Create your models here.
