from django.shortcuts import render, get_object_or_404
from .models import Posts

def home(request):
    return render(request, 'blog/home.html')

def about_us(request):
    return render(request, 'blog/about.html')





def blog_home(request):
    # Pass the blog post to the template
    posts = get_object_or_404(Posts)
    return render(request, 'blog/blogs.html', {'posts': posts})


def blog(request, url):
    # Search for the blog post by its name
    post = get_object_or_404(Posts, slug=url)  # Adjust 'title' to your model's field

    # Pass the blog post to the template
    return render(request, 'blog/blog.html', {'post': post})










def contactanos(request):
    return render(request, 'blog/contactanos.html')

def login(request):
    return render(request, 'blog/login.html')

def register(request):
    return render(request, 'blog/register.html')

def categorias(request):
    return render(request, 'blog/categorias.html')