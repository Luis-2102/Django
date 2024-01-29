# en forms.py
from django import forms

class RentaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    tipo_vehiculo = forms.ChoiceField(label='Tipo de Vehículo', choices=[])

    # Agrega otros campos según sea necesario
    precio = forms.DecimalField(label='Precio', decimal_places=2)

    def __init__(self, *args, **kwargs):
        pages = kwargs.pop('pages', [])
        super(RentaForm, self).__init__(*args, **kwargs)
        self.fields['tipo_vehiculo'].choices = [(page.title, page.title) for page in pages]
