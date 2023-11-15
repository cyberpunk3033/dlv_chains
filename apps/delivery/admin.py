

from django.contrib import admin
from .models import (BaseChain, TypeDelivery,
                     AllDeliveryTypeWeight,
                     OtherVariant, Calculation,
                     PriceDelivery, DeliveryLSKTSTP, BrandChain)
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget

#region BASE FUNCTIONS AND CLASSES
class AddAdminPanel:
    def __init__(self,models_:tuple):
        self.models_=models_
    def views_admin_panel(self):
        for model in self.models_:
            admin.site.register(model)

    def imp_exp_model_data(model_):
        class Base_Resource(resources.ModelResource):
            class Meta:
                model = model_

        class Base_Admin(ImportExportModelAdmin):
            resource_class = Base_Resource

        admin.site.register(model_, Base_Admin)
# endregion

# !!! add model for import and export in admin site panel
tuple_models_imp_exp=(BaseChain,BrandChain,OtherVariant)

# !!! add model for views admin site panel
tuple_models_adm_pnl=(AllDeliveryTypeWeight,Calculation,PriceDelivery,DeliveryLSKTSTP)




