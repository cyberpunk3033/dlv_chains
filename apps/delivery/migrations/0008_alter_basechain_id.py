# Generated by Django 4.2.7 on 2023-11-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_remove_basechain_days_basechain_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basechain',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
