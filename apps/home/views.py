from django.shortcuts import render
from django.http import HttpResponse
# fom models import

# Create your views here.


def home_view(request):
    return HttpResponse('Bienvenido a la página Principal')
