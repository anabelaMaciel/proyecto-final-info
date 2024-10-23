from django.shortcuts import render
from django.forms import ModelForm
from django import forms
from .models import Comentarios, Categorias, Posts

from .models import Usuario_personalizado
from django.contrib.auth.forms import UserCreationForm

# En nuestra clase Meta definimos el modelo, con el cual va a interactuar nuestro formulario
# y los campos que vamos a permitir que completen los usuarios


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario_personalizado
        fields = ['username', 'email', 'password1', 'password2']


# Formulario de Categorias
class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'imagen']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario_personalizado
        fields = ['username', 'email', 'password1', 'password2']
# Formulario de Posts


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['slug', 'titulo', 'subtitulo', 'cuerpo',
                  'categorias', 'imagen', 'usuario']

# Formulario de Comentarios


class ComentForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']

# Formulario de Contactanos


class ContactanosForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    # Asegúrate de usar 'message' aquí
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
