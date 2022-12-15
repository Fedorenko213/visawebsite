from django.contrib import admin
from VisaWebsite import settings
from .models import Visa, VisaTariff, VisaCountry, VisaType, VisaStatus, User


class VisaAdmin(admin.ModelAdmin):
    list_display = ('code_visa', 'username', 'first_name', 'surname', 'visa_type',  'tariff_number', 'status')


admin.site.register(User)
admin.site.register(Visa, VisaAdmin)
admin.site.register(VisaTariff)
admin.site.register(VisaType)
admin.site.register(VisaCountry)
admin.site.register(VisaStatus)


