# Generated by Django 3.0.3 on 2020-11-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0021_auto_20201030_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]