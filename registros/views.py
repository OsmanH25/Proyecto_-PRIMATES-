from django.shortcuts import render, redirect #importamos el render para poder renderizar las vistas y el redirect para poder redireccionar a otras paginas
from .models import Registro #importamos el modelo de la clase Registro que va a ser la base de datos
from .forms import RegistroForm #importamos el formulario de la clase RegistroForm que va a ser el formulario de la pagina de editar registros
# Create your views here.
#EN ESTE ARCHIVO SE CREAN LAS VISTAS DE LA APLICACION EN ESTE CASO "REGISTROS" CON HTML
#ACA SE CREAN LAS FUNCIONES QUE SE LLAMAN EN EL ARCHIVO urls.py
def portada_index(request):
    return render(request, 'portada_index.html')

def listar_registros(request):
    registro = Registro.objects.all() # con esto le decimos que nos traiga todos los registros de la base de datos y rempleza a "SELECT * FROM registros_registro"
    return render(request, 'listar_registros.html',{'registros': registro}) #aca le decimos que nos renderice la pagina "listar_registros.html" y que nos muestre los registros de la base de datos
def crear_registros(request):
    registro = Registro(nombre=request.POST['nombre'], descripcion=request.POST['descripcion']) #aca le decimos que cree un nuevo registro con los datos que le pasamos por el formulario
    registro.save() #aca le decimos que guarde el registro creado anteriormente en la base de datos
    return redirect('registros') #aca le decimos que nos redireccione a la pagina principal "registros"

def eliminar_registros(request, registros_id):
    eliminar_registros = Registro.objects.get(id=registros_id) #aca le decimos que nos traiga el registro que queremos eliminar
    eliminar_registros.delete()
    return redirect('registros') #aca le decimos que nos redireccione a la pagina principal "registros"

def editar_registros(resquest, registros_id):
    registro = Registro.objects.get(id=registros_id)
    forms = RegistroForm(resquest.POST or None, instance=registro) #
    if forms.is_valid() and resquest.POST: #aca le decimos que si el formulario es valido y se envio el formulario
        forms.save()
        return redirect('registros')
    return render(resquest, "editar_diagnostico.html", {'forms': forms}) #aca le decimos que nos renderice la pagina "editar_diagnostico.html" y que nos muestre el formulario de editar registros


#Este archivo es para crear las funciones que se van a llamar en el archivo urls.py y que se van a mostrar en el navegador