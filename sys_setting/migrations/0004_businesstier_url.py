# Generated by Django 3.0.3 on 2020-10-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_setting', '0003_silvertier'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstier',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
