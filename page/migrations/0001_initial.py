# Generated by Django 3.0.6 on 2020-05-17 02:11

import ckeditor.fields
from django.db import migrations, models
import linguist.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_az', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('text_az', ckeditor.fields.RichTextField(null=True)),
                ('text_en', ckeditor.fields.RichTextField(null=True)),
                ('text_ru', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(linguist.mixins.ModelMixin, models.Model),
        ),
    ]
