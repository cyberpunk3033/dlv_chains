# Generated by Django 4.2.7 on 2023-11-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_remove_basechain_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='basechain',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]