from django.shortcuts import render, get_object_or_404
from .models import Posts, Comentarios

def home(request):
    return render(request, 'blog/home.html')

def about_us(request):
    return render(request, 'blog/about.html')









def blog(request):
    posts = Posts.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


def noticia(request, url):
    post = get_object_or_404(Posts, slug=url)
    coms = Comentarios.objects.filter(post=post)
    return render(request, 'blog/noticia.html', {
        'post': post, 
        'comentarios': coms
    })









def contactanos(request):
    return render(request, 'blog/contactanos.html')

def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')

def categorias(request):
    return render(request, 'blog/categorias.html')