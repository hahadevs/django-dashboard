from django.contrib import admin
from organizationapp.models import *
# Register your models here.

admin.site.register(OrganizationDetails)
admin.site.register(locationDetails)
admin.site.register(billingDetails)
admin.site.register(YearlyPlans)