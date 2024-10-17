from typing import Any
from django import forms
from .models import Eventos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2'
        )




    """ def clean(self):
        data = super().clean()
        password1 = data['password1']
        password2 = data['password2']

        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return data"""
        
class EventoForm(forms.ModelForm):
    
    class Meta:
        model = Eventos
        fields = ['titulo','descripcion','fecha','ubicacion']
        widgets = {'fecha': forms.DateInput(attrs={'type':'date'}),}
