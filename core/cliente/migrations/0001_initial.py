# Generated by Django 3.1 on 2020-09-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=15)),
                ('usermod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'db_table': 'Cliente',
            },
        ),
    ]