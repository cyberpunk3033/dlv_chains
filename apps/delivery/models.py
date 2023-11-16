from django.db import models
from abc import ABC, abstractmethod

#region BASE FUNCTIONS AND CLASSES

#endregion

#region ДОСТАВКА
class TypeDelivery(models.Model): # Тип доставки - морская и тд

    name_delivery=models.CharField(verbose_name='Тип доставки',max_length=50)
    code_delivery = models.CharField(verbose_name='Код доставки', max_length=50, help_text='',default="LS")
    duty=models.FloatField(verbose_name='Гос. пошлина у.е.',default=300)
    def __str__(self):
        return self.name_delivery

    class Meta:
        verbose_name = 'Варианты доставки'
        verbose_name_plural = 'Варианты доставки'


class DeliveryRate(models.Model):
    type_delivery = models.ForeignKey(TypeDelivery, on_delete=models.CASCADE)
    weight = models.FloatField(verbose_name='Вес тон.',default=0)
    rate = models.FloatField(verbose_name='Коэффициент',default=0)
    price = models.FloatField(verbose_name='Стоимость',default=0)

    class Meta:
        verbose_name = 'Стоимость доставки'
        verbose_name_plural = 'Стоимость доставки'

    def str(self):
        return f'{self.type_delivery}' #TODO: Исправить отображение в общем списке
#endregion

#region ЦЕПИ

class BaseChain(models.Model):
    GOST_ISO_DIN = (
        ('MGOST', 'M ГОСТ 588-81'),
          ('MISO1977','M ISO 1977'),
          ('MTISO1977','MT ISO 1977'),
          ('FVDIN','FV DIN'),
          ('FVТDIN', 'FVТ DIN'),
          ('FVCDIN','FVC DIN'),
          ('ZDIN', 'Z DIN'),
          ('ZEDIN','ZE DIN'),
          ('ZCDIN','ZC DIN'),
    )
    name_chains = models.CharField(verbose_name='Название цепи', max_length=50, help_text='')
    standard=models.CharField(verbose_name='Стандарт', max_length=13, choices=GOST_ISO_DIN)
    weight=models.FloatField(verbose_name='Вес',null=True)
    rate=models.FloatField(verbose_name='Коэффициент')


    class Meta:

        verbose_name="Базовая цепь"
        verbose_name_plural="Базовые цепи"

    def __str__(self):
        return self.name_chains

class BrandChain(models.Model):
    name_brand=models.CharField(verbose_name='Брэнд цепи', max_length=50, help_text='')
    def __str__(self):
        return self.name_brand

class OtherVariant(models.Model):
    TYPE_OF_PROCESSING=(

        ('NOP', 'без обработки'),
        ('ZN', 'оцинковка(ZN)'),
        ('NP', 'никелирование(NP)'),
        ('DR', 'горячая оцинковка(DR)'),
        ('GM', 'покрытие цепи геомет(GM)'),
        ('SS', 'нержавейка(SS)'),

    )

    brand=models.ForeignKey(BrandChain, on_delete=models.CASCADE,default=1)
    type_processing=models.CharField(verbose_name='Тип обработки цепи', max_length=30, help_text='',choices=TYPE_OF_PROCESSING,default='NOP')
    km_field = models.FloatField(verbose_name='Стоимость кг. дол. США',default=1)
    days=models.IntegerField(verbose_name='Дней на изготовление', help_text='',default=70)
    margin =models.FloatField(verbose_name='Маржа',default=1)

    def __str__(self):
        return f' {self.brand}-{self.type_processing}-{self.km_field}-{self.days}-{self.margin}'
    class Meta:
        verbose_name='Дополнительные варианты обработки'
        verbose_name_plural='Дополнительные варианты обработки'


#endregion

class Calculation(models.Model):
    pass

class PriceDelivery(models.Model):
    pass

class DeliveryLSKTSTP(models.Model):
    pass








