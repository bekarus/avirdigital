# Generated by Django 2.1.7 on 2019-04-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190405_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='blog'),
        ),
    ]