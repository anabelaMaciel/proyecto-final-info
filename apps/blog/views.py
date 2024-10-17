from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.http import JsonResponse
from .models import Posts, Comentarios, Like_comentario, Like_post, Usuario_personalizado


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
    is_like_post = Like_post.objects.filter(post=post, usuario=request.user)
    total_likes = len(Like_post.objects.filter(post=post))
    
    if len(is_like_post) == 0:
        is_like_post = False
    print(is_like_post)
        
    return render(request, 'blog/noticia.html', {
        'total_likes': total_likes,
        'is_like_post': is_like_post,
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


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    like, created = Like_post.objects.get_or_create(post=post, usuario=request.user)

    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('noticia', args=[post.slug]) + '#like_post')


@login_required
def like_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, id=comentario_id)
    like, created = Like_comentario.objects.get_or_create(comentario=comentario, usuario=request.user)

    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('noticia', args=[comentario.post.slug]))