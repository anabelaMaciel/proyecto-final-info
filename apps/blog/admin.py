from django.contrib import admin
from .models import Categorias, Usuario_personalizado, Posts, Like_post, Comentarios, Like_comentario

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'imagen']

class PostAdmin(admin.ModelAdmin):
    list_display = ['fecha_creacion', 'usuario', 'categorias', 'subtitulo', 'titulo']

class Usuario_personalizadoAdmin(admin.ModelAdmin):
    list_display = ['fecha_registro', 'username', 'email', 'is_staff', 'is_superuser']

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ['post', 'usuario', 'contenido', 'fecha_comentario']

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Usuario_personalizado, Usuario_personalizadoAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(Like_post)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Like_comentario)
