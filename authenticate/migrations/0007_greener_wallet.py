# Generated by Django 4.1.7 on 2023-04-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0006_rename_point_greener_greener_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='greener',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]