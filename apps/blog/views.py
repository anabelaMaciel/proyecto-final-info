from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about_us(request):
    return render(request, 'blog/about.html')

def contactanos(request):
    return render(request, 'blog/contactanos.html')

def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')

def categorias(request):
    return render(request, 'blog/categorias.html')