# Generated by Django 2.1.7 on 2019-04-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20190402_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='subservice',
            name='icon',
            field=models.CharField(default='Null', max_length=255),
        ),
    ]
