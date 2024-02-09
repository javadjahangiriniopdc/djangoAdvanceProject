from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    fullname = models.CharField(max_length=50)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'fullname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
