from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about_us(request):
    return render(request, 'blog/about.html')

def contactanos(request):
    return render(request, 'blog/contactanos.html')