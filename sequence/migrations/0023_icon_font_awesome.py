# Generated by Django 3.0.3 on 2020-09-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0022_remove_icon_font_awesome'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='font_awesome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]