from rest_framework import serializers
from .models import EmergencyType, Emergency, VehicleEmergency, Role
from .models import UserAssistance, FireCode


class EmergencyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyType
        fields = ('id', 'title', 'description')


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ('id', 'latitude', 'longitude', 'start_time', 'finish_time',
                  'emergency_type')


class VehicleEmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleEmergency
        fields = ('id', 'latitude', 'longitude', 'start_time', 'finish_time',
                  'emergency')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'description')


class UserAssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAssistance
        fields = ('id', 'user', 'vehicle_emergency', 'role', 'leader')


class FireCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireCode
        fields = ('id', 'code', 'description')
