from rest_framework import serializers
from .models import VehicleType, Vehicle


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('id', 'title', 'description')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'code', 'model', 'brand', 'motor', 'vehicule_year',
                  'seat_number', 'vehicule_type')
