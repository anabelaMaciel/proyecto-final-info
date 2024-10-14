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


def post_detail(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
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
