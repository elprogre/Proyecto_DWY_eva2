from django.contrib import admin
from django.urls import path, include
from .views import pagina_principal, galeria, formulario, nosotros, productos, login, logout_vista, lista_productos, eliminar_productos, busqueda_mod, modificar_producto

urlpatterns = [
    path('', pagina_principal, name='INIC'),
    path('galeria/', galeria, name='GALE'),
    path('formulario/', formulario, name='FORM'),
    path('nosotros/', nosotros, name='NOSO'),
    path('productos/', productos, name='PROD'),
    path('login/', login, name='LOGI'),
    path('logout_vista/', logout_vista, name='LOGO'),
    path('lista_productos/', lista_productos, name='LISTAP'),
    path('eliminar_producto/<id>/', eliminar_productos, name='ELIMINARP'),
    path('buscar_producto/<id>/', busqueda_mod, name='BUSCARP'),
    path('modificar_productos/', modificar_producto, name='MODIFICARP'),
]
