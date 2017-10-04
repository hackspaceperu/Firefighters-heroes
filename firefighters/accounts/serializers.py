from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'dni', 'phone', 'cell_phone',
                  'address', 'birthdate')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
