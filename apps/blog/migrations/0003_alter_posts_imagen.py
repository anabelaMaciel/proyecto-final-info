<<<<<<< HEAD
# Generated by Django 5.1.2 on 2024-10-15 04:29
=======
# Generated by Django 5.1.2 on 2024-10-16 03:43
>>>>>>> 901211d8a8c1ebbea931df0f4a35b578255e7ce0

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='imagen',
            field=models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='news'),
        ),
    ]
