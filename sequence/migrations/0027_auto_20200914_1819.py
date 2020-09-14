# Generated by Django 3.0.3 on 2020-09-14 17:19

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0026_image_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='captured_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='coordinates_cas',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='coordinates_image',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='geometry_coordinates',
            field=django.contrib.gis.db.models.fields.LineStringField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='geometry_coordinates_ary',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=1), size=None), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='seq_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='user_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
