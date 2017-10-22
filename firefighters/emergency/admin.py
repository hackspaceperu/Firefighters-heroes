from django.contrib import admin

# Register your models here.
from .models import EmergencyType, Emergency, VehicleEmergency, Role
from .models import UserAssistance, FireCode

admin.site.register(EmergencyType)
admin.site.register(Emergency)
admin.site.register(VehicleEmergency)
admin.site.register(Role)
admin.site.register(UserAssistance)
admin.site.register(FireCode)
