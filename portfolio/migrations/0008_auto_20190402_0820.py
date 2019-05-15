# Generated by Django 2.1.7 on 2019-04-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20190402_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliocategory',
            name='slug_az',
        ),
        migrations.RemoveField(
            model_name='portfoliocategory',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='portfoliocategory',
            name='slug_ru',
        ),
        migrations.AddField(
            model_name='portfoliocategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]