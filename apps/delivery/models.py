from django.db import models
from abc import ABC, abstractmethod

#region BASE FUNCTIONS AND CLASSES

class ModelsTemplate(models.Model):
    @abstractmethod
    def __str__(self):
        pass

    class Meta:
        abstract = True

#endregion




# Create your models here.
#region ДОСТАВКА
class TypeDelivery(ModelsTemplate): # Тип доставки - морская и тд

    name_delivery=models.CharField(verbose_name='Тип доставки',max_length=50, help_text='')

    def __str__(self):
        return self.name_delivery


class AllDeliveryTypeWeight(ModelsTemplate): # Вес с коэффициентами
    DELIVERY_CODE = (
        ('LS', 'LS'),
        ('LT', 'LT'),
        ('LR', 'LR'),
        ('LA', 'LA'),
    )
    id_name_delivery=models.ForeignKey(TypeDelivery, on_delete=models.CASCADE)
    code_delivery=models.CharField(verbose_name='Код',max_length=3, choices=DELIVERY_CODE)
    weight=models.FloatField(verbose_name='Вес')
    ratio=models.FloatField(verbose_name='Коэффициент')

#endregion



#region ЦЕПИ

class BaseChain(ModelsTemplate):
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
    gost_iso_din=models.CharField(verbose_name='Стандарт', max_length=13,choices=GOST_ISO_DIN)
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
        ('GM', 'геомет(GM)'),
        ('SS', 'нержавейка(SS)'),

    )

    brand=models.ForeignKey(BrandChain, on_delete=models.CASCADE,default=1)
    type_processing=models.CharField(verbose_name='Тип обработки цепи', max_length=30, help_text='',choices=TYPE_OF_PROCESSING,default='NOP')
    km_field = models.FloatField(verbose_name='Стоимость кг. дол. США',default=1)
    days=models.IntegerField(verbose_name='Дней на изготовление', help_text='',default=70)
    margin =models.FloatField(verbose_name='Маржа',default=1)

    def __str__(self):
        return f' {self.brand}-{self.type_processing}-{self.km_field}-{self.days}-{self.margin}'


#endregion

class Calculation(models.Model):
    pass

class PriceDelivery(models.Model):
    pass

class DeliveryLSKTSTP(models.Model):
    pass








