# Generated by Django 3.0.3 on 2020-09-27 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0008_auto_20200918_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='business_email',
        ),
    ]