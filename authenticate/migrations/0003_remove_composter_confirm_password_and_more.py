# Generated by Django 4.1.7 on 2023-03-11 05:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_composter_confirm_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composter',
            name='confirm_password',
        ),
        migrations.AlterField(
            model_name='composter',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
