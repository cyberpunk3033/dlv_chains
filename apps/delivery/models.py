from django.db import models

# Create your models here.
#region ДОСТАВКА
class TypeDelivery(models.Model): # Тип доставки - морская и тд

    name_delivery=models.CharField(verbose_name='Тип доставки',max_length=50, help_text='')

    def __str__(self):
        return self.name_delivery


class AllDeliveryTypeWeight(models.Model): # Вес с коэффициентами
    DELIVERY_CODE = (
        ('LS', 'LR'),
        ('LT', 'LA'),
    )
    id_name_delivery=models.ForeignKey(TypeDelivery, on_delete=models.CASCADE)
    code_delivery=models.CharField(verbose_name='Код', choices=DELIVERY_CODE)
    weight=models.FloatField(verbose_name='Вес')
    ratio=models.FloatField(verbose_name='Коэффициент')

#endregion



#region ЦЕПИ

class BaseChain(models.Model):
    GOST_ISO_DIN = (
        ('M ГОСТ 588-81', 'M ISO 1977'),
        ('MT ISO 1977', 'FV DIN'),
        ('FVТ DIN', 'FVC DIN'),
        ('Z DIN', 'ZE DIN'),
        ('ZC DIN', ''),
    )
    name_chains = models.CharField(verbose_name='Название цепи', max_length=50, help_text='')
    gost_iso_din=models.CharField(verbose_name='Код', choices=GOST_ISO_DIN)
    days=models.IntegerField(verbose_name='Дней доставки', max_length=3)

class OtherVariant(models.Model):
    name_brand=models.CharField(verbose_name='Брэнд цепи', max_length=50, help_text='')
    type_chain=models.CharField(verbose_name='Тип цепи', max_length=3, help_text='')
    km_field = models.FloatField()
    pm_field=models.IntegerField(verbose_name='Дней', max_length=3, help_text='')
    mm_field=models.FloatField()

#endregion

class Calculation(models.Model):
    pass

class PriceDelivery(models.Model):
    pass

class DeliveryLSKTSTP(models.Model):
    pass








