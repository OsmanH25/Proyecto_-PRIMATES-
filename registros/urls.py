from django.urls import path  # importamos el path para poder crear las rutas
from .views import portada_index,listar_registros, crear_registros, eliminar_registros, editar_registros # importamos las funciones creadas en views- . -py
urlpatterns = [
    path('', portada_index, name='portada_index'), #aca se crea la ruta de la pagina principal
    path('registros', listar_registros, name='registros'), #aca se crea la ruta de la pagina de registros
    path('crear/', crear_registros, name='crear_registros'),
    path('eliminar_registros/<int:registros_id>/', eliminar_registros, name='eliminar_registros'), #aca se crea la ruta de la pagina de eliminar registros
    path('editar_registros/<int:registros_id>/', editar_registros, name='editar_registros'), #aca se crea la ruta de la pagina de editar registros
]
#Aca se llaman las funciones creadas eSn views.py para ser mostradas en el navegador

# este archivo es el que se encarga de crear las rutas de la aplicacion para que se puedan ver en el navegador y poder navegar por la aplicacion