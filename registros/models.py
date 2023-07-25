from django.db import models #importamos el modelo de la base de datos que trae django para poder crear las tablas de la base de datos

# Create your models here.
class Registro(models.Model): #aca se crea la clase Registro que hereda de models.Model que es el modelo de la base de datos
    nombre = models.CharField(max_length=100)  # esto nos va a decir que el texto que vamos a ingresar es obligatorio
    descripcion = models.TextField(blank=True)  # esto nos va a decir que el texto que vamos a ingresar es opcional


# con " python manage.py migrate " se crean las tablas en la base de datos
# con " python manage.py makemigrations " se migran las tablas creadas a la basse de datos

# este archivo es el que se encarga de crear la base de datos y las tablas para la aplicacion