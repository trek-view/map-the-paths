# Generated by Django 3.0.3 on 2020-10-19 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sequence', '0011_delete_mapfeaturedetection'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapFeatureDetection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_key', models.CharField(blank=True, max_length=100, null=True)),
                ('detection_key', models.CharField(blank=True, max_length=100, null=True)),
                ('user_key', models.CharField(blank=True, max_length=100, null=True)),
                ('map_feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sequence.MapFeature')),
            ],
        ),
    ]