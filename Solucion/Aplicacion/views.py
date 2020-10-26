from django.shortcuts import render
from .models import Slider, Galeria, MisionyVision, Productos
# importar la tabla de usuario desde el administrador
from django.contrib.auth.models import User
# Importar librerias de autentificacion
from django.contrib.auth import authenticate, logout, login as login_aute
# Agregar una decoracion que permite evitar el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def pagina_principal(request):
    slider = Slider.objects.all()
    return render(request,'web/pagina_principal.html',{'lista_slider':slider})


def galeria(request):
    foto = Galeria.objects.all()
    return render(request,'web/galeria.html',{'lista_fotos':foto})

def formulario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUsuario")
        clave1 = request.POST.get("txtPass")
        clave2 = request.POST.get("txtPass2")
        try:
            u = User.objects.get(username=usuario) #select * from user where username=usuario
            mensaje="Usuario Existe"
            return render(request, 'web/formulario.html', {'msg':mensaje})
        except:
            if clave1 != clave2:
                mensaje="Contraseñas Incorrectas"
                return render(request, 'web/formulario.html', {'msg':mensaje})
            u = User()
            u.first_name = nombre
            u.last_name = apellido
            u.email = correo
            u.username = usuario
            u.set_password(clave1)
            u.save()
            us = authenticate(request, username=usuario, password=clave1)
            login_aute(request,us)
            return render(request, 'web/pagina_principal.html', {'user':us})
    return render(request,'web/formulario.html')


def nosotros(request):
    texto = MisionyVision.objects.all()
    return render(request,'web/nosotros.html',{'lista_texto':texto})

@login_required(login_url='/login/')
@permission_required('Aplicacion.delete_productos', login_url='/login/')
def eliminar_productos(request, id):
    try:
        producto = Productos.objects.get(nombre=id)
        producto.delete()
        msg='Producto Eliminado'
    except expression as identifier:
        msg='No Elimino Producto'
    productos = Productos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_productos':productos, 'msg':msg})


@login_required(login_url='/login/')
@permission_required('Aplicacion.view_productos', login_url='/login/')
def lista_productos(request):
    productos = Productos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_productos':productos})

@login_required(login_url='/login/')
@permission_required('Aplicacion.add_productos', login_url='/login/')
def productos(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        producto = Productos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        )
        producto.save()
        return render(request,'web/productos.html',{'msg':'Producto Guardado'})
    return render(request,'web/productos.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        password = request.POST.get("txtPass")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aute(request,us)
            slider = Slider.objects.all()
            return render(request, 'web/pagina_principal.html',{'lista_slider':slider})
        else:
            return render(request, 'web/login.html', {'msg':'Clave Incorrecta'})
    return render(request,'web/login.html')

def logout_vista(request):
    logout(request)
    slider = Slider.objects.all()
    return render(request, 'web/pagina_principal.html',{'lista_slider':slider})

@login_required(login_url='/login/')
@permission_required('Aplicacion.view_productos', login_url='/login/')
def busqueda_mod(request, id):
    try:
        producto = Productos.objects.get(nombre=id)
        return render(request,'web/productos_actualizar.html',{'producto':producto})
    except:
        msg='Producto NO Encontrado'
    productos = Productos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_productos':productos, 'msg':msg})

@login_required(login_url='/login/')
@permission_required('Aplicacion.view_productos', login_url='/login/')
@permission_required('Aplicacion.change_productos', login_url='/login/')
def modificar_producto(request):
    msg=''
    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        try:
            producto = Productos.objects.get(nombre=nombre)
            producto.precio = precio
            producto.descripcion = descripcion
            producto.stock = stock
            producto.save()
            msg='Producto Modificado'
        except:
            msg='Producto NO Modificado'
            
    productos = Productos.objects.all()
    return render(request,'web/admin_productos.html',{'lista_productos':productos, 'msg':msg})