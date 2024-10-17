# Generated by Django 5.1.2 on 2024-10-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='imagen',
            field=models.ImageField(default='static/post_default.png', upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='imagen',
            field=models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='news'),
        ),
    ]
