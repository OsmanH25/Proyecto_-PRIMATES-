from django.forms import ModelForm #importamos el ModelForm para poder crear formularios
from .models import Registro #Importamos el modelo  de la clase Registro

class RegistroForm(ModelForm): #aqui se crea la nueva clase RegistroForm que hereda de ModelForm que es el formulario de la clase Registro
    class Meta: #aqui se crea la clase Meta que es para decirle que campos va a tener el formulario
        model = Registro #aqui se le dice que el modelo de la clase RegistroForm es el modelo de la clase Registro
        fields = '__all__' #aqui se le dice que los campos o caracteristicas de la clase RegistroForm son todos los que estan en la clase Registro