from django.shortcuts import render
from django.forms import ModelForm
from django import forms
from .models import Comentarios, Categorias, Posts

from .models import Usuario_personalizado
from django.contrib.auth.forms import UserCreationForm

# En nuestra clase Meta definimos el modelo, con el cual va a interactuar nuestro formulario
# y los campos que vamos a permitir que completen los usuarios

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'imagen']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario_personalizado
        fields = ['username', 'email', 'password1', 'password2']

def listar_categorias(request):
    categorias = []

    # Manejar el formulario si es que se envía
    if request.method == 'POST':
        form = CategoriasForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo objeto de categoría
            form.save()
            # Recuperar todas las categorías solo si se ha enviado el formulario
            categorias = Categorias.objects.all()
    else:
        form = CategoriasForm()

    return render(request, 'listar_categorias.html', {'form': form, 'categorias': categorias})


# Formulario de Posts
class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo', 'subtitulo', 'cuerpo', 'categorias', 'imagen']
        # categorias deplegable que muestre trodas las categorias que ya esten creadas en mi bd
        # categorias sea un desplegable que consuma el modelo de categorias .
# {{form_as.p}} ...pegar en el template. css toquen...forms.. submit


# Formulario de Comentarios
class ComentForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['usuario', 'contenido']
