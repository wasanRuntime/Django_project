from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager( BaseUserManager):
    """Helps user work with our custome user model"""
    #def create_user(self):
    def create_user(self, email, name, password=None, **extra_fields):
        """Creates a new user profile"""
        if not email:
            raise ValueError("User Must have email address.")
        email = self.normalize_email(email)
        user = self.model(email = email, name = name, **extra_fields)

        user.set_password(password)
        user.save(using = self._db)

        return user
    def create_superuser(self, email, name, password = None, **extra_fields):
        """Creates and saves new superuser with given details"""
        #user = self.create_user(email, name, password=password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)

        #user.is_superuser = True
        #user.is_staff = True

        #user.save(using = self._db)

        #return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This class represent user profile inside our system"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get users full name"""

        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """django uses this when itneeds to convert object into a string"""

        return self.email
