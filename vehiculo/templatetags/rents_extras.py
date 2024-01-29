from django import template
from vehiculo.models import Rent

register = template.Library()

@register.simple_tag
def get_Rents_list():
    Rents = Rent.objects.all()
    return Rents