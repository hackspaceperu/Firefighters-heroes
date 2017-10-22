from django.contrib import admin

# Register your models here.
from .models import VehicleType, Vehicle, EquipamentOxigen

admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(EquipamentOxigen)
