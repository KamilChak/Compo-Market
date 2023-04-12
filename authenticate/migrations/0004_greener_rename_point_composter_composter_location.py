# Generated by Django 4.1.7 on 2023-04-07 22:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_remove_composter_confirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=12)),
                ('lastName', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.RenameField(
            model_name='composter',
            old_name='point',
            new_name='composter_location',
        ),
    ]
