from django.contrib import admin
from .models import Slider, Galeria, MisionyVision, Productos

#USUARIO ADMIN: nico
#CONTRASEÑA ADMIN: 123456


# Register your models here.
class LavadosAdminGaleria(admin.ModelAdmin):
    list_display=['identif','nombre','imagen']
    search_fields=['identif','nombre']
    list_per_page = 10

class LavadosAdminMisionVision(admin.ModelAdmin):
    list_display=['identif','mision','vision']
    search_fields=['identif']
    list_per_page = 10

class LavadosAdminMProductos(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre']
    list_per_page = 10


admin.site.register(Slider, LavadosAdminGaleria)
admin.site.register(Galeria, LavadosAdminGaleria)
admin.site.register(MisionyVision, LavadosAdminMisionVision)
admin.site.register(Productos, LavadosAdminMProductos)