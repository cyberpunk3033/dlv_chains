# Generated by Django 4.2.7 on 2023-11-13 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_alter_basechain_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basechain',
            name='weight',
        ),
    ]