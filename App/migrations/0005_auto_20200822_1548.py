# Generated by Django 3.1 on 2020-08-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20200822_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarterback',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='quarterback',
            name='position',
            field=models.CharField(max_length=3),
        ),
    ]
