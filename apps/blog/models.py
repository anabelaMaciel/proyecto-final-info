from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager

# Create your models here.
# Categorias


class Categorias(models.Model):
    nombre = models.CharField(max_length=40, null=False)
    imagen = models.ImageField(
        upload_to='imagenes/', null=False, blank=False, default='blog/post_default.png')

    def __str__(self):
        return self.nombre

# Usuario


class Usuario_personalizado(AbstractUser):
    fecha_registro = models.DateField(auto_now_add=True)
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['username']

    def __str__(self):
        return self.username

# Post


class Posts(models.Model):
    slug = models.CharField(max_length=40, null=True, unique=True)
    titulo = models.CharField(max_length=40, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    cuerpo = models.TextField(null=False)
    categorias = models.ForeignKey(
        Categorias, on_delete=models.SET_NULL, null=True, default='sin categoria')
    usuario = models.ForeignKey(
        Usuario_personalizado, on_delete=models.CASCADE)
    imagen = models.ImageField(
        null=True, blank=True, upload_to='news')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"  # nombre en singular
        verbose_name_plural = "Posts"  # nombre en plural
        # ordena por fecha de creacion, de mas reciente a mas antiguo
        ordering = ['-fecha_creacion']
        # asegura que un autor no pueda tener dos posts con el mismo titulo
        unique_together = ('titulo', 'usuario')

    def __str__(self):
        return self.titulo

    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

# Like_post
class Like_post(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        Usuario_personalizado, on_delete=models.CASCADE)
    fecha_like = models.DateField(auto_now_add=True)

# Asegura que un usuario solo pueda dar "me gusta" una vez a un post
    class Meta:
        unique_together = ('usuario', 'post')

    def __str__(self):
        return f"{self.usuario.username} likes {self.post.titulo}"


# Comentarios
class Comentarios(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario_personalizado, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=500)
    fecha_comentario = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(Usuario_personalizado, related_name='comment_likes', blank=True)

    def __str__(self):
        return self.contenido

    def total_likes(self):
        return self.likes.count()

# Like_comentario


class Like_comentario(models.Model):
    comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        Usuario_personalizado, on_delete=models.CASCADE)
    fecha_like = models.DateField(auto_now_add=True)

# Asegura que un usuario solo pueda dar "me gusta" una vez a un comentario
    class Meta:
        unique_together = ('usuario', 'comentario')

    def __str__(self):
        return f"{self.usuario.username} likes {self.comentario.post.titulo}"
