# Generated by Django 3.0.3 on 2020-10-30 17:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sys_setting', '0004_businesstier_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sequence', '0019_auto_20201029_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_key', models.CharField(blank=True, max_length=100, null=True, verbose_name='Mapillary User Key')),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('google_street_view', models.BooleanField(default=False)),
                ('strava', models.CharField(blank=True, max_length=50, null=True)),
                ('tag', models.ManyToManyField(to='sys_setting.Tag')),
                ('transport_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sequence.TransType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
