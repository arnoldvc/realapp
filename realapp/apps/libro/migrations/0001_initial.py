# Generated by Django 3.2.9 on 2022-04-06 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=220)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
