# Generated by Django 2.1.7 on 2019-04-02 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_subservice_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service'),
        ),
    ]