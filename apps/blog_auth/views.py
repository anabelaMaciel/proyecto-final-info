from django.shortcuts import render
from django.views.generic import FormView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
# Create your views here.
# CBV


class SignUpView(FormView):
    template_name = "registration/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("apps.blog_auth:login")

    def def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    next_page = "home"
