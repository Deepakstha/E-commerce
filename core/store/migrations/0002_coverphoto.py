# Generated by Django 3.1 on 2023-05-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(upload_to='photo/cover_photos')),
            ],
        ),
    ]
