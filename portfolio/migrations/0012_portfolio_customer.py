# Generated by Django 2.1.7 on 2019-04-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20190404_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='customer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]