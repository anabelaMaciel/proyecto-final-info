# Generated by Django 5.1.2 on 2024-10-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='imagen',
            field=models.ImageField(default='static/post_default.png', upload_to='imagenes/'),
        ),
    ]