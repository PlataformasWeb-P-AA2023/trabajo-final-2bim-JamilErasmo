# Generated by Django 4.2.2 on 2023-07-28 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('siglas', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LocalRepuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('comida', models.CharField(max_length=30)),
                ('ventas', models.IntegerField()),
                ('permiso', models.IntegerField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.barrio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='LocalComida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('comida', models.CharField(max_length=30)),
                ('ventas', models.FloatField()),
                ('permiso', models.IntegerField()),
                ('barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.barrio')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.persona')),
            ],
        ),
    ]
