# Generated by Django 3.2.16 on 2022-12-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUsine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infoUsineArLink', models.FileField(upload_to='InfoUsine/Ar/')),
                ('infoUsineFrLink', models.FileField(upload_to='InfoUsine/Fr/')),
                ('creationTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]