from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Posts, Categorias, Comentarios, Like_comentario, Like_post, Usuario_personalizado
from .forms import CategoriasForm, PostForm, ComentForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'blog/home.html')

def about_us(request):
    return render(request, 'blog/about.html')

def blog(request):
    todos_posts = Posts.objects.all()
    return render(request, 'blog/blog.html', {'posts': todos_posts})

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

# def listar_noticias(request):
#     category = categorias.GET.get('categoria')
#     if category:
#         noticias = Posts.objects.filter(categoria_nombre = category)
#     else:
#         noticias = Posts.objects.all()    

def contactanos(request):
    return render(request, 'blog/contactanos.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = Usuario_personalizado.objects.get(email=email)
        except Usuario_personalizado.DoesNotExist:
            user_obj = None

        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logueado con éxito!')
                return redirect('blog-home')
        
        messages.error(request, 'Datos incorrectos.')
    return render(request, 'blog/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            group = Group.objects.get_or_create(name="Registrado")
            user.groups.add(group)
            
            login(request, user)
            messages.success(request, 'Cuenta creada con éxito!')
            return redirect('blog-home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserRegisterForm()

    return render(request, 'blog/register.html', {'form': form})

def categorias(request):
    todas_categorias = Categorias.objects.all()
    return render(request, 'blog/categorias.html', {"categorias": todas_categorias})


# @login_required
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    like, created = Like_post.objects.get_or_create(
        post=post, usuario=request.user)

    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('noticia', args=[post.slug]) + '#like_post')


# @login_required
def like_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, id=comentario_id)
    like, created = Like_comentario.objects.get_or_create(
        comentario=comentario, usuario=request.user)

    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('noticia', args=[comentario.post.slug]))

# CRUD de Categorías, Posts y Comentarios
# con CBV


# Crear Categorías

class CrearCategoriasView(CreateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'blog/form_categorias.html'
    success_url = reverse_lazy('categorias')


# Editar Categoría


class EditarCategoriasView(UpdateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = "blog/form_categorias.html"
    success_url = reverse_lazy('categorias')

# Eliminar Categoría


class EliminarCategoriasView(DeleteView):
    model = Categorias
    template_name = "blog/form_eliminar.html"
    success_url = reverse_lazy("categorias")


# Crear Posts


class CrearPostsView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'blog/form_posts.html'
    success_url = reverse_lazy('blog')

# Editar Posts


class EditarPostsView(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "blog/form_posts.html"
    success_url = reverse_lazy("blog")

# Eliminar Posts


class EliminarPostsView(DeleteView):
    model = Posts
    template_name = "blog/form_eliminar.html"
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
    form_class = ComentForm
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
