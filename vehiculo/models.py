from django.db import models
from ckeditor.fields import RichTextField
from pages.models import Page
from django.urls import reverse


#class codigo_descuento(models.Model):
#    code = models.CharField(max_length=10)
#    porcentaje_descuento = models.DecimalField(max_digits=3, decimal_places=2)

#    def __str__(self):
#        return self.code 

class Rent(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    ciudad_recogida = models.CharField(max_length=50)
    ciudad_devolucion = models.CharField(max_length=50)
    fecha_renta = models.DateField()
    fecha_devolucion = models.DateField()
    tipo_vehiculo = models.OneToOneField(Page, on_delete=models.SET_NULL, null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    content = RichTextField(verbose_name="Contenido")
    codigo_descuento = models.CharField(max_length=5, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Formulario de renta"
        verbose_name_plural = "Formularios de renta"
        ordering = ['order', 'fecha_renta']

    def __str__(self):
        return f"Rent: {self.ciudad_recogida} - {self.ciudad_devolucion}"

    def get_absolute_url(self):
        return reverse('rents:rent', args=[str(self.id)])
