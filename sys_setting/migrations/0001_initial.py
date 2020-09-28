# Generated by Django 3.0.3 on 2020-09-28 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed for Username.')])),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_actived', models.BooleanField(default=True)),
            ],
        ),
    ]
