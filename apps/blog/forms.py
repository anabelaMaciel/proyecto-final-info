from django.forms import ModelForm
from .models import Comentarios


class ComentForm(ModelForm):
     class Meta:
         model = Comentarios
         fields = ('usuario', 'contenido')