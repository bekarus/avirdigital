# Generated by Django 2.1.7 on 2019-04-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_auto_20190404_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='position',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]