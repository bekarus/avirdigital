# Generated by Django 2.1.7 on 2019-03-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190328_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
