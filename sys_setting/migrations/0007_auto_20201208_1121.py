# Generated by Django 3.0.3 on 2020-12-08 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sys_setting', '0006_delete_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='silvertier',
            name='user',
        ),
        migrations.DeleteModel(
            name='GoldTier',
        ),
        migrations.DeleteModel(
            name='SilverTier',
        ),
    ]
