# Generated by Django 2.1.7 on 2019-04-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20190329_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='name',
            new_name='image_description',
        ),
        migrations.RemoveField(
            model_name='service',
            name='text',
        ),
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='sub_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(default='Null', max_length=255),
            preserve_default=False,
        ),
    ]