# Generated by Django 4.2.7 on 2023-11-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0014_rename_gost_iso_din_basechain_standard_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='othervariant',
            options={'verbose_name': 'Дополнительные варианты обработки', 'verbose_name_plural': 'Дополнительные варианты обработки'},
        ),
        migrations.AlterModelOptions(
            name='typedelivery',
            options={'verbose_name': 'Варианты доставки', 'verbose_name_plural': 'Варианты доставки'},
        ),
        migrations.AddField(
            model_name='typedelivery',
            name='code_delivery',
            field=models.CharField(default=False, max_length=50, verbose_name='Код доставки'),
        ),
    ]