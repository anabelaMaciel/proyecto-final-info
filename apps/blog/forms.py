from django.forms import ModelForm
from .models import Comentarios, Categorias, Posts

# En nuestra clase Meta definimos el modelo, con el cual va a interactuar nuestro formulario
# y los campos que vamos a permitir que completen los usuarios

# Formulario de Categorias


class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = ('nombre', 'imagen')


# Formulario de Posts
class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ('titulo', 'subtitulo', 'cuerpo', 'categorias', 'imagen')


# Formulario de Comentarios
class ComentForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ('usuario', 'contenido')

