# Generated by Django 2.2 on 2020-06-14 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del producto')),
                ('precio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Precio del producto')),
                ('cantidad', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cantidades del producto')),
                ('montoadicional', models.CharField(blank=True, max_length=200, null=True, verbose_name='Monto adicional')),
                ('imagen', models.ImageField(blank=True, max_length=200, null=True, upload_to='', verbose_name='Imagen del producto')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
