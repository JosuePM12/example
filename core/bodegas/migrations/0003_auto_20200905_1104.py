# Generated by Django 3.1.1 on 2020-09-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0002_auto_20200905_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
