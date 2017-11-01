from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'document', 'phone', 'cell_phone',
                  'address', 'birthdate', 'role')
        read_only_fields = ('register_date', )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
          setattr(instance, key, value)

        if password is not None:
          instance.set_password(password)

        instance.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'title', 'description')
