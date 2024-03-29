from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, first_name, last_name, is_superuser, is_staff, **extra_fields):
        email = self.normalize_email(email)

        if not first_name:
            raise ValueError('The first_name is required')
        if not last_name:
            raise ValueError('The last_name is required')

        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name,
                          is_superuser=is_superuser, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password, first_name, last_name, **extra_fields):
        return self._create_user(username, email, password, first_name, last_name, False, False, **extra_fields)

    def create_superuser(self, username, email, password, first_name, last_name, **extra_fields):
        return self._create_user(username, email, password, first_name, last_name, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(null=True, blank=True, max_length=8, validators=[MinLengthValidator(8)])
    birthdate = models.DateField(null=True, blank=True)
    registration_date = models.DateField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=9)
    cell_phone = models.CharField(null=True, blank=True, max_length=9)
    address = models.CharField(null=True, blank=True, max_length=250)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name+' '+self.last_name
