# Generated by Django 2.2 on 2020-06-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='producto/', verbose_name='Imagen del producto'),
        ),
    ]