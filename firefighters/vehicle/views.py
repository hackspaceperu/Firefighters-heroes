from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import VehicleType, Vehicle
from .serializers import VehicleTypeSerializer, VehicleSerializer

# Create your views here.


class VehicleTypeListView(ListCreateAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleTypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleListView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
