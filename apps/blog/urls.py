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
from .views import CrearComentariosView, EditarComentariosView, EliminarComentariosView, EditarCategoriasView, CrearCategoriasView, EliminarCategoriasView, CrearPostsView, EditarPostsView, EliminarPostsView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about_us, name='about-us'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('like/<int:comentario_id>/',
         views.like_comentario, name='like_comentario'),

    path('blog/', views.blog, name='blog'),
    path('blog/crear/', CrearPostsView.as_view(),
         name='crear_post'),  # Nueva url para CREAR
    # path('blog/<str:url>/', views.noticia, name='noticia'),
    # VER RUTA DESPUES DEL BLOG/
    path('blog/<int:id>/', views.noticia, name='noticia'),

    path('contactanos/', views.contactanos, name='contactanos'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # MOSTRAR Categorias
    path('categorias/', views.categorias, name='categorias'),
    # CREAR Categoria
    path('categorias/crear/', CrearCategoriasView.as_view(), name='crear_categoria'),

    # EDITAR categoria
    path('categorias/editar/<int:pk>',
         EditarCategoriasView.as_view(), name='editar_categoria'),

    # ELIMINAR Categoria
    path('categorias/eliminar/<int:pk>', EliminarCategoriasView.as_view(),
         name='eliminar_categoria'),

    # EDITAR post
    path('blog/editar/<int:pk>',
         EditarPostsView.as_view(), name='editar_post'),

    # ELIMINAR post
    path('blog/eliminar/<int:pk>', EliminarPostsView.as_view(),
         name='eliminar_post'),

    path('comentario/crear/', CrearComentariosView.as_view(), name='crear_coment'),

    # EDITAR post
    path('comentario/editar/',
         EditarComentariosView.as_view(), name='editar_coment'),

    # ELIMINAR post
    path('comentario/eliminar/', EliminarComentariosView.as_view(),
         name='eliminar_coment'),

]
