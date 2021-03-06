# Generated by Django 3.1.1 on 2020-09-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=15)),
                ('usermod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'bodegas',
                'verbose_name_plural': 'bodegas',
                'db_table': 'Bodega',
            },
        ),
    ]
