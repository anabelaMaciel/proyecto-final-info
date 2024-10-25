from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Posts, Categorias, Comentarios, Like_comentario, Like_post, Usuario_personalizado
from .forms import CategoriasForm, PostForm, ComentForm,ContactoForm,UserRegisterForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from .forms import EditarPerfilForm
from .models import Usuario_personalizado
from .forms import UserRegisterForm
from django.contrib import messages


# Vistas de la aplicación
def home(request):
    return render(request, 'blog/home.html')


def about_us(request):
    return render(request, 'blog/about.html')


def success(request):
    return render(request, 'blog/success.html')


def contactanos(request):
    return render(request, 'contacto.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            # Enviar el correo electrónico
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            send_mail(
                f'Nuevo mensaje de contacto: {asunto}',
                f'Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}',
                email,  # De (remitente)
                ['tecnofilosinformatorio@gmail.com'],  # Para (destinatario)
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = ContactoForm()

    data = {
        'form': form
    }
    return render(request, 'contacto.html', data)


"""def contacto(request):
    data = {
        'form': ContactoForm()
    }
    return render(request, 'contacto.html', data)

"""
"""def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje en la base de datos
            contacto = form.save()

            # Enviar el correo
            subject = f"Nuevo mensaje de contacto: {contacto.asunto}"
            message = f"Nombre: {contacto.nombre}\nEmail: {contacto.email}\n\nMensaje:\n{contacto.mensaje}"
            recipient_list = ['tecnofilos.xtech@hotmail.com']
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER, recipient_list)

            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            # Redirige a la misma página o a otra que desees
            return redirect('contacto')
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})"""


"""def contactanos_view(request):
    if request.method == 'POST':
        form = ContactanosForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data.get('message', '')

            try:
                send_mail(
                    f'Mensaje de {name}',
                    message,
                    email,
                    ['tecnofilos.xtech@hotmail.com'],
                )
                return redirect('/success')
            except BadHeaderError:
                return HttpResponse('Encabezado de correo no válido.')
    else:
        form = ContactanosForm()

    return render(request, 'blog/form_contactanos.html', {'form': form})"""


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
                return redirect('blog-home')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        else:
            messages.error(request, 'No existe un usuario con este correo.')

    return render(request, 'blog/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            group, created = Group.objects.get_or_create(name="Registrado")
            user.groups.add(group)

            login(request, user) 
            messages.success(request, '¡Cuenta creada con éxito!')
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


def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    like, created = Like_post.objects.get_or_create(
        post=post, usuario=request.user)

    if not created:
        like.delete()
    return HttpResponseRedirect(reverse('noticia', args=[post.slug]) + '#like_post')

def editar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST['username']
        user.email = request.POST['email']

        if request.POST.get('quitar_imagen'):
            user.imagen_perfil.delete()  
        elif 'imagen_perfil' in request.FILES:
            user.imagen_perfil = request.FILES['imagen_perfil']

        user.save()
        messages.success(request, 'Perfil actualizado con éxito.')
        return redirect('editar_perfil')

    return render(request, 'blog/editar_perfil.html')


@login_required
def like_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentarios, id=comentario_id)
    user = request.user

    if user in comentario.likes.all():
        comentario.likes.remove(user)
    else:
        comentario.likes.add(user)

    return redirect(reverse('noticia', kwargs={'url': comentario.post.slug}))


# CRUD de Categorías, Posts y Comentarios con CBV

# Categorías
class CrearCategoriasView(CreateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'blog/form_categorias.html'
    success_url = reverse_lazy('categorias')


class EditarCategoriasView(UpdateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = "blog/form_categorias.html"
    success_url = reverse_lazy('categorias')


class EliminarCategoriasView(DeleteView):
    model = Categorias
    template_name = "blog/form_eliminar.html"
    success_url = reverse_lazy("categorias")


# Posts
class ListarPostsView(ListView):
    model = Posts
    template_name = 'blog/blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Posts.objects.all()
        categoria = self.request.GET.get('categoria')
        search_query = self.request.GET.get('q')
        orden = self.request.GET.get('orden')

        if categoria:
            queryset = queryset.filter(categorias__nombre=categoria)

        if search_query:
            queryset = queryset.filter(titulo__icontains=search_query)

        if orden == 'ascendente':
            queryset = queryset.order_by('titulo')
        elif orden == 'descendente':
            queryset = queryset.order_by('-titulo')
        elif orden == 'antiguedad':
            queryset = queryset.order_by('fecha_creacion')
        elif orden == 'recientes':
            queryset = queryset.order_by('-fecha_creacion')
        else:
            queryset = queryset.order_by('-fecha_creacion')

        return queryset


class CrearPostsView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'blog/form_posts.html'
    success_url = reverse_lazy('blog')


class EditarPostsView(UpdateView):
    model = Posts
    form_class = PostForm
    template_name = "blog/form_posts.html"
    success_url = reverse_lazy("blog")


class EliminarPostsView(DeleteView):
    model = Posts
    template_name = "blog/form_eliminar.html"
    success_url = reverse_lazy("blog")


# Comentarios
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


class CrearComentariosView(CreateView):
    model = Comentarios
    form_class = ComentForm
    template_name = 'blog/form_coment.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        post_id = self.kwargs['post_id']
        form.instance.post = get_object_or_404(Posts, id=post_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('noticia', kwargs={'url': self.object.post.slug})


class EditarComentariosView(UpdateView):
    model = Comentarios
    form_class = ComentForm
    template_name = "blog/form_coment.html"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.post = self.object.post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('noticia', kwargs={'url': self.object.post.slug})


class EliminarComentariosView(DeleteView):
    model = Comentarios
    template_name = "blog/form_eliminar.html"

    def get_success_url(self):
        return reverse('noticia', kwargs={'url': self.object.post.slug})


def noticia(request, url):
    post = get_object_or_404(Posts, slug=url)
    coms = Comentarios.objects.filter(post=post).prefetch_related(
        Prefetch('likes', queryset=Usuario_personalizado.objects.only('id'))
    )

    is_like_post = Like_post.objects.filter(post=post, usuario=request.user).exists(
    ) if request.user.is_authenticated else False
    total_likes = Like_post.objects.filter(post=post).count()

    return render(request, 'blog/noticia.html', {
        'total_likes': total_likes,
        'is_like_post': is_like_post,
        'post': post,
        'comentarios': coms,
        'user': request.user
    })
