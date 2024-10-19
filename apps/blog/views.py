from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categorias, Posts, Comentarios, Like_comentario, Like_post, Usuario_personalizado
from .forms import CategoriaForm, PostForm, ComentForm
from django.db.models.query import QuerySet
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


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

# CRUD de Categorías, Posts y Comentarios
# con CBV

# Filtrar Categorías por Título


class ListarCategoriasView(ListView):
    model = Categorias
    template_name = 'categorias/lista_categorias.html'
    context_object_name = 'categorias'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("name")
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)

        return queryset.order_by('name')

# Crear Categorías


class CrearCategoriasView(CreateView):
    model = Categorias
    form_class = CategoriaForm
    template_name = 'categorias/form_categorias.html'
    success_url = reverse_lazy('lista_categorias')

# Leer Categoría


class DetalleCategoriasView(DetailView):
    model = Categorias
    context_object_name = 'categorias'
    template_name = 'categorias/detalle_categorias.html'

# Editar Categoría
class CategoriasUpdateView(UpdateView):
    model = Categorias
    fields = ['nombre']
    template_categorias = "categorias_form.html"
    redireccion = reverse_lazy("categorias")

# Eliminar Categoría


class EliminarCategoriasView(DeleteView):
    model = Categorias
    template_name = "categorias/confirmacion_eliminacion.html"
    success_url = reverse_lazy("lista_categorias")

# Filtrar Posts por Título


class ListarPostsView(ListView):
    model = Posts
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("titulo")
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)

        return queryset.order_by('titulo')

# Crear Posts


class CrearPostsView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/form_posts.html'
    success_url = reverse_lazy('lista_posts')

# Leer Posts


class DetallePostsView(DetailView):
    model = Posts
    context_object_name = 'Posts'
    template_name = 'posts/detalle_posts.html'

# Editar Posts


class ActualizarPostsView(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "posts/form_posts.html"
    success_url = reverse_lazy("lista_posts")

# Eliminar Posts


class EliminarPostsView(DeleteView):
    model = Posts
    template_name = "posts/confirmacion_eliminacion.html"
    success_url = reverse_lazy("lista_posts")

# Filtrar Comentarios por Título


class ListarComentariosView(ListView):
    model = Comentarios
    template_name = 'comentarios/lista_comentarios.html'
    context_object_name = 'comentarios'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("titulo")
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)

        return queryset.order_by('titulo')

# Crear Comentarios


class CrearComentariosView(CreateView):
    model = Comentarios
    form_class = CategoriaForm
    template_name = 'comentarios/form_comentarios.html'
    success_url = reverse_lazy('lista_comentarios')

# Leer Comentarios


class DetalleComentariosView(DetailView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = 'comentarios/detalle_comentarios.html'

# Editar Comentarios


class ActualizarComentariosView(UpdateView):
    model = Comentarios
    form_class = ComentForm
    template_name = "comentarios/form_comentarios.html"
    success_url = reverse_lazy("lista_comentarios")

# Eliminar Comentario


class EliminarComentariosView(DeleteView):
    model = Comentarios
    template_name = "comentarios/confirmacion_eliminacion.html"
    success_url = reverse_lazy("lista_comentarios")
