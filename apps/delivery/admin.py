from django.contrib import admin
from .models import (BaseChain, TypeDelivery,

                     OtherVariant, Calculation,
                     PriceDelivery, DeliveryLSKTSTP,
                     BrandChain,TypeDelivery,DeliveryRate)
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets

#region BASE FUNCTIONS AND CLASSES

def views_admin_panel(models_:tuple):

    for model in models_:
        admin.site.register(model)

def imp_exp_model_data(models_:tuple):
    #list_filter_=('',)

    for model_ in models_:

        class Base_Resource(resources.ModelResource):
            class Meta:
                model = model_

        class Base_Admin(ImportExportModelAdmin):
            resource_class = Base_Resource
           # list_filter=list_filter_

        admin.site.register(model_, Base_Admin)

# endregion

# !!! tuple models for import and export in admin site panel
tuple_models_imp_exp=(BaseChain,BrandChain,OtherVariant,DeliveryRate)

imp_exp_model_data(tuple_models_imp_exp)

# !!!tuple models for views admin site panel
tuple_models_adm_pnl=(Calculation,
                      PriceDelivery,DeliveryLSKTSTP,TypeDelivery)

views_admin_panel(tuple_models_adm_pnl)


