from django.db import models
from vehicle.models import Vehicle
from accounts.models import User


# Create your models here.
STATUS_CHOICES = (('A', 'ACTIVE'),
                  ('D', 'DEACTIVE'),
                  ('E', 'ELIMINATED'))


class EmergencyType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('register_date',)


class Emergency(models.Model):
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    emergency_type = models.ForeignKey(EmergencyType)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')

    class Meta:
        ordering = ('register_date',)


class VehicleEmergency(models.Model):
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    emergency = models.ForeignKey(Emergency)
    vehicle = models.ForeignKey(Vehicle)

    class Meta:
        ordering = ('register_date',)


class Role(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')

    class Meta:
        ordering = ('register_date',)


class UserAssistance(models.Model):
    register_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    user = models.ForeignKey(User)
    vehicle_emergency = models.ForeignKey(VehicleEmergency)
    leader = models.CharField(max_length=1, choices=(('F', 'NO'), ('T', 'SI')),
                              default='F')
    role = models.ForeignKey(Role)

    class Meta:
        ordering = ('register_date',)


class FireCode(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('register_date',)
