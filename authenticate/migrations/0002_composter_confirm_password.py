# Generated by Django 4.1.7 on 2023-03-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='composter',
            name='confirm_password',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
