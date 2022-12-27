# Generated by Django 3.2.16 on 2022-12-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryNameArab', models.CharField(max_length=50)),
                ('categoryNameFrench', models.CharField(max_length=50)),
                ('categoryNameEnglish', models.CharField(max_length=50)),
                ('creationTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='GalleryPhotos/')),
                ('creationTime', models.DateTimeField(auto_now_add=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GalleryPhotos.gallery')),
            ],
        ),
    ]