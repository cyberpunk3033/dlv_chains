# Generated by Django 4.2.7 on 2023-11-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_remove_typedelivery_days_typedelivery_duty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryrate',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Вес тон.'),
        ),
        migrations.DeleteModel(
            name='AllDeliveryTypeWeight',
        ),
    ]