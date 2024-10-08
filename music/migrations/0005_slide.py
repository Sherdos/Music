# Generated by Django 5.1 on 2024-08-22 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_music_author_music_image_music_views_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide/', verbose_name='слайд')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
