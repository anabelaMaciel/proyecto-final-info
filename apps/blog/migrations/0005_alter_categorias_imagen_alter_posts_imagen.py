# Generated by Django 5.1.2 on 2024-10-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comentarios_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='imagen',
            field=models.ImageField(default='apps/blog/static/post_default.png', upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen',
            field=models.ImageField(blank=True, default='apps/blog/static/post_default.png', null=True, upload_to='news'),
        ),
    ]
