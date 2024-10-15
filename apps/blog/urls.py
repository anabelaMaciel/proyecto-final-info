"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about_us, name='about-us'),

    path('blog/', views.blog, name='blog'),
    path('blog/<str:url>/', views.noticia, name='noticia'),

    path('contactanos/', views.contactanos, name='contactanos'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('categorias/', views.categorias, name='categorias'),

    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('like_comentario/<int:comentario_id>/',
         views.like_comentario, name='like_comentario'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
