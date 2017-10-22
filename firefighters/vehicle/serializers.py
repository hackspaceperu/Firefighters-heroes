from rest_framework import serializers
from .models import VehicleType, Vehicle, EquipamentOxigen


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('id', 'title', 'description')


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('id', 'code', 'model', 'brand', 'motor', 'vehicule_year',
                  'seat_number', 'vehicule_type')

    def create(self, validated_data):
        vehicle = Vehicle(code=validated_data.get('code'),
                          model=validated_data.get('model'),
                          brand=validated_data.get('brand'),
                          motor=validated_data.get('motor'),
                          vehicule_year=validated_data.get('vehicule_year'),
                          seat_number=validated_data.get('seat_number'),
                          vehicule_type=validated_data.get('vehicule_type'))
        vehicle.save()
        return vehicle


class EquipamentOxigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipamentOxigen
        fields = ('id', 'code', 'title', 'description', 'capacity')
