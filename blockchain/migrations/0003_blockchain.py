# Generated by Django 4.1.7 on 2023-04-12 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_block_alter_transaction_recipient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.JSONField(default=list)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transactions', models.ManyToManyField(to='blockchain.transaction')),
            ],
        ),
    ]