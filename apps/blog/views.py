from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
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
<<<<<<< HEAD
=======
"""from django.shortcuts import render, get_object_or_404
from .models import Categorias, Usuario_personalizado, Posts, Like_post, Comentarios, Like_comentario
from .forms import ComentForm


def home(request):
    categorias = Categorias.objects.all()
    return render(request, 'blog/home.html', {'categorias': categorias})


def categorias_posts(request, categorias_id):
    categoria = get_object_or_404(Categorias, id=categorias_id)
    posts = categoria.posts.all()
    return render(request, 'blog/categoria_posts.html', {'category': categoria, 'posts': posts})
>>>>>>> 8685baf252db92be1267e62ef970bae0c000ebc0


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
<<<<<<< HEAD
    comentarios = Comentarios.objects.filter(post=post)
    context = {
        'post': post,
        'comentarios': comentarios,
    }
    return render(request,  'noticia.html', context)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    like, created = Like_post.objects.get_or_create(
        post=post, usuario=request.user)
    if not created:
        # Si ya existe un like del usuario, eliminarlo (deshacer el like)
        like.delete()
    return redirect('post_detail', post_id=post.id)


@login_required
def like_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, id=comentario_id)
    like, created = Like_comentario.objects.get_or_create(
        comentario=comentario, usuario=request.user)
    if not created:
        # Si ya existe un like del usuario, eliminarlo (deshacer el like)
        like.delete()
        liked = False
    else:
        liked = True
    return Jsonresponse({'liked': liked, 'total_likes': comentario.likes.count()})
=======
    return render(request, 'blog/post_detail.html', {'post': post})

"""
"""# Create your views here.
def index (request):
    post = Posts.objects.all()
    
def post_detail (request, post_id):
    post = Posts.objects.get(id = post_id)
    
    comentario = post.comentarios.filter (active=True)
    
    if request.method == 'POST':
        formulario = ComentForm (request.POST)
        
#Validamos si el formulario tiene todos los datos         
        
        if formulario.is_valid(): 
            nuevo_formulario = formulario.save(commit=False)  
#commit=False es para que el comentario se guarde una vez terminado y no mientras se va escribiendo. 
    
return render (request= 'post_detail.html',{'post':post})
"""
>>>>>>> 8685baf252db92be1267e62ef970bae0c000ebc0
