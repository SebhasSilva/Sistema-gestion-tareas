from django.db import models #Importa models

class Task(models.Model): #Se defina el modelo task, que hereda la clase models.Model
    title = models.CharField(max_length=100) #Define el limite de caracteres del titulo
    description = models.TextField() #Define un campo de texto
    created_at = models.DateTimeField(auto_now_add=True) #Define fecha y hora en que se crea la tarea
    STATUS_CHOICES = [
        ('P', 'Pendiente'),
        ('E', 'En progreso'),
        ('C', 'Completada'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES) #Almacenara solo un caracter de los definidos

    def __str__(self):
        return self.title