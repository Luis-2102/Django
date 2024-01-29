from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Rent

# Create your views here.
class RentListView(ListView):
    model = Rent
    
class RentDetailView(DetailView):
    model = Rent

class RentCreate(CreateView):
    model = Rent
    fields = ['nombre','apellido', 'cedula','telefono' ,'tipo_vehiculo','content','order', 'ciudad_recogida', 'ciudad_devolucion', 'fecha_renta', 'fecha_devolucion', 'codigo_descuento']
    success_url = reverse_lazy('rents:rents')
    
class RentUpdateView(UpdateView):
    model = Rent
    fields = ['nombre','apellido', 'cedula','telefono', 'tipo_vehiculo','content','order', 'ciudad_recogida', 'ciudad_devolucion', 'fecha_renta', 'fecha_devolucion', 'codigo_descuento']
    success_url = reverse_lazy('rents:rents')
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_fields'] = ['image', 'precio']  
        return context
    

    
class RentDeleteView(DeleteView):
    model = Rent
    success_url = reverse_lazy("rents:rents")
