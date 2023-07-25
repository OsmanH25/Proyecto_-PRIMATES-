from django.apps import AppConfig #importamos la clase AppConfig


class RegistrosConfig(AppConfig): #Aca se configura el nombre de la app
    default_auto_field = 'django.db.models.BigAutoField' #Aca se configura el tipo de campo de la base de datos
    name = 'registros' #Aca se configura el nombre de la app
