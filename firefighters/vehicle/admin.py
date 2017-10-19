from django.contrib import admin

# Register your models here.
from .models import VehicleType, Vehicle

admin.site.register(VehicleType)
admin.site.register(Vehicle)
