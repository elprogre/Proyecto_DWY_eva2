# Generated by Django 2.2.16 on 2020-10-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('identif', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('identif', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='fotos')),
            ],
        ),
    ]
