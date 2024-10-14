from django.contrib import admin

from .models import Categorias, Usuario_personalizado, Posts, Like_post, Comentarios, Like_comentario
admin.site.register(Categorias)
admin.site.register(Usuario_personalizado)
admin.site.register(Posts)
admin.site.register(Like_post)
admin.site.register(Comentarios)
admin.site.register(Like_comentario)

