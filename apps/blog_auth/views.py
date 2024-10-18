from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import SignUpForm, EventoForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .models import Eventos
# Create your views here.
# CBV


class SignUpView(FormView):
    template_name = "registration/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("apps.blog_auth:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    next_page = "home"


class CrearEventoView(CreateView):
    model = Eventos
    form_class = EventoForm
    template_name = 'eventos/form_evento.html'
    success_url = reverse_lazy('lista_eventos')


class DetalleEventoView(DetailView):
    model = Eventos
    context_object_name = 'evento'
    template_name = 'eventos/detalle_evento.html'


class ListarEventosView(ListView):
    model = Eventos
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("titulo")
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)

        return queryset.order_by('titulo')


class ActualizarEventoView(UpdateView):
    model = Eventos
    form_class = EventoForm
    template_name = "eventos/form_evento.html"
    success_url = reverse_lazy("lista_eventos")


class EliminarEventoView(DeleteView):
    model = Eventos
    template_name = "eventos/confirmacion_eliminacion.html"
    success_url = reverse_lazy("lista_eventos")
