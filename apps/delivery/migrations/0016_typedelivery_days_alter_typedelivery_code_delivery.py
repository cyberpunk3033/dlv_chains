# Generated by Django 4.2.7 on 2023-11-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_alter_othervariant_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='typedelivery',
            name='days',
            field=models.CharField(default='60', max_length=50, verbose_name='Код доставки'),
        ),
        migrations.AlterField(
            model_name='typedelivery',
            name='code_delivery',
            field=models.CharField(default='LS', max_length=50, verbose_name='Код доставки'),
        ),
    ]
