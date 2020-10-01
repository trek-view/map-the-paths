# Generated by Django 3.0.3 on 2020-09-29 17:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0004_auto_20200929_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='SequenceWeather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location_country', models.CharField(blank=True, max_length=100, null=True)),
                ('location_region', models.CharField(blank=True, max_length=100, null=True)),
                ('location_timezone_id', models.CharField(blank=True, max_length=100, null=True)),
                ('location_lat', models.FloatField(default=0)),
                ('location_lon', models.FloatField(default=0)),
                ('location_localtime', models.CharField(blank=True, max_length=100, null=True)),
                ('location_localtime_epoch', models.IntegerField(default=0)),
                ('location_utc_offset', models.CharField(blank=True, max_length=100, null=True)),
                ('current_observation_time', models.TimeField(blank=True, null=True)),
                ('current_temperature', models.IntegerField(default=0)),
                ('current_weather_code', models.IntegerField(default=0)),
                ('current_weather_icons', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), blank=True, null=True, size=None)),
                ('current_weather_descriptions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=100), blank=True, null=True, size=None)),
                ('current_wind_speed', models.IntegerField(default=0)),
                ('current_wind_degree', models.IntegerField(default=0)),
                ('current_wind_dir', models.CharField(blank=True, max_length=100, null=True)),
                ('current_pressure', models.IntegerField(default=0)),
                ('current_precip', models.IntegerField(default=0)),
                ('current_humidity', models.IntegerField(default=0)),
                ('current_cloudcover', models.IntegerField(default=0)),
                ('current_feelslike', models.IntegerField(default=0)),
                ('current_uv_index', models.IntegerField(default=0)),
                ('current_visibility', models.IntegerField(default=0)),
                ('current_is_day', models.CharField(blank=True, max_length=50, null=True)),
                ('his_date', models.DateField(blank=True, null=True)),
                ('his_date_epoch', models.IntegerField(default=0)),
                ('his_astro_sunrise', models.TimeField(blank=True, null=True)),
                ('his_astro_sunset', models.TimeField(blank=True, null=True)),
                ('his_astro_moonrise', models.TimeField(blank=True, null=True)),
                ('his_astro_moonset', models.TimeField(blank=True, null=True)),
                ('his_astro_moon_phase', models.CharField(blank=True, max_length=50, null=True)),
                ('his_mintemp', models.IntegerField(default=0)),
                ('his_maxtemp', models.IntegerField(default=0)),
                ('his_avgtemp', models.IntegerField(default=0)),
                ('his_totalsnow', models.IntegerField(default=0)),
                ('his_sunhour', models.IntegerField(default=0)),
                ('his_uv_index', models.IntegerField(default=0)),
                ('his_hourly_time', models.IntegerField(default=0)),
                ('his_hourly_temperature', models.IntegerField(default=0)),
                ('his_hourly_wind_speed', models.IntegerField(default=0)),
                ('his_hourly_wind_degree', models.IntegerField(default=0)),
                ('his_hourly_wind_dir', models.CharField(blank=True, max_length=50, null=True)),
                ('his_hourly_weather_code', models.IntegerField(default=0)),
                ('his_hourly_weather_icons', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), blank=True, null=True, size=None)),
                ('his_hourly_weather_descriptions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=100), blank=True, null=True, size=None)),
                ('his_hourly_precip', models.IntegerField(default=0)),
                ('his_hourly_humidity', models.IntegerField(default=0)),
                ('his_hourly_visibility', models.IntegerField(default=0)),
                ('his_hourly_pressure', models.IntegerField(default=0)),
                ('his_hourly_cloudcover', models.IntegerField(default=0)),
                ('his_hourly_heatindex', models.IntegerField(default=0)),
                ('his_hourly_dewpoint', models.IntegerField(default=0)),
                ('his_hourly_windchill', models.IntegerField(default=0)),
                ('his_hourly_windgust', models.IntegerField(default=0)),
                ('his_hourly_feelslike', models.IntegerField(default=0)),
                ('his_hourly_chanceofrain', models.IntegerField(default=0)),
                ('his_hourly_chanceofremdry', models.IntegerField(default=0)),
                ('his_hourly_chanceofwindy', models.IntegerField(default=0)),
                ('his_hourly_chanceofovercast', models.IntegerField(default=0)),
                ('his_hourly_chanceofsunshine', models.IntegerField(default=0)),
                ('his_hourly_chanceoffrost', models.IntegerField(default=0)),
                ('his_hourly_chanceofhightemp', models.IntegerField(default=0)),
                ('his_hourly_chanceoffog', models.IntegerField(default=0)),
                ('his_hourly_chanceofsnow', models.IntegerField(default=0)),
                ('his_hourly_chanceofthunder', models.IntegerField(default=0)),
                ('his_hourly_uv_index', models.IntegerField(default=0)),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sequence.Sequence')),
            ],
        ),
    ]