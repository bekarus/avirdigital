# Generated by Django 2.1.7 on 2019-04-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_auto_20190402_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(max_length=255, null=True),
        ),
    ]