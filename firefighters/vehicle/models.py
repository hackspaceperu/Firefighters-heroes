from django.db import models

# Create your models here.
STATUS_CHOICES = (('A', 'ACTIVE'),
                  ('D', 'DEACTIVE'),
                  ('E', 'ELIMINATED'))


class VehicleType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('register_date',)


class Vehicle(models.Model):
    code = models.CharField(max_length=20)
    model = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50)
    motor = models.CharField(max_length=50, blank=True, null=True)
    vehicule_year = models.CharField(max_length=5, blank=True, null=True)
    seat_number = models.CharField(max_length=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              default='A')
    register_date = models.DateTimeField(auto_now_add=True)
    vehicule_type = models.ForeignKey(VehicleType)

    class Meta:
        ordering = ('register_date',)
