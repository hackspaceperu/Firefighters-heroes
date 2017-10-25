from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import EmergencyType, Emergency, VehicleEmergency, Role
from .models import UserAssistance, FireCode
from .serializers import EmergencyTypeSerializer, EmergencySerializer
from .serializers import VehicleEmergencySerializer, RoleSerializer
from .serializers import UserAssistanceSerializer, FireCodeSerializer


class EmergencyTypeListView(ListCreateAPIView):
    queryset = EmergencyType.objects.all()
    serializer_class = EmergencyTypeSerializer


class EmergencyTypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EmergencyType.objects.all()
    serializer_class = EmergencyTypeSerializer


class EmergencyListView(ListCreateAPIView):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer


class EmergencyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer


class VehicleEmergencyListView(ListCreateAPIView):
    queryset = VehicleEmergency.objects.all()
    serializer_class = VehicleEmergencySerializer


class VehicleEmergencyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleEmergency.objects.all()
    serializer_class = VehicleEmergencySerializer


class RoleListView(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserAssistanceListView(ListCreateAPIView):
    queryset = UserAssistance.objects.all()
    serializer_class = UserAssistanceSerializer


class UserAssistanceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserAssistance.objects.all()
    serializer_class = UserAssistanceSerializer


class FireCodeListView(ListCreateAPIView):
    queryset = FireCode.objects.all()
    serializer_class = FireCodeSerializer


class FireCodeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = FireCode.objects.all()
    serializer_class = FireCodeSerializer
