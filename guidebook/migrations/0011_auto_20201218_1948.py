# Generated by Django 3.0.3 on 2020-12-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebook', '0010_auto_20201218_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poiexternalurl',
            options={'ordering': ['external_url']},
        ),
        migrations.RemoveField(
            model_name='poiexternalurl',
            name='poi',
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='external_url',
            field=models.ManyToManyField(to='guidebook.POIExternalURL'),
        ),
    ]
