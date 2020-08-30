# Generated by Django 3.0.3 on 2020-08-30 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0016_remove_transtype_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='transtype',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sequence.Icon'),
        ),
    ]