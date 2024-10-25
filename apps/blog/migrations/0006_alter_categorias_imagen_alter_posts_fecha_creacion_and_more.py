# Generated by Django 5.1.2 on 2024-10-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categorias_imagen_alter_posts_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='imagen',
            field=models.ImageField(default='blog/post_default.png', upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen',
            field=models.ImageField(blank=True, default='blog/post_default.png', null=True, upload_to='news'),
        ),
    ]
