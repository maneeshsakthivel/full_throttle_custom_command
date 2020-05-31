from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=254, default="")
    middle_name = models.CharField(max_length=254, blank=True, default="")
    last_name = models.CharField(max_length=254, default="")
    timezone = models.CharField(max_length=10, default="")

    USERNAME_FIELD = 'id'

    def __str__(self):
        return self.first_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    login_time = models.DateTimeField(default=datetime.strptime("31/12/9999 23:59:59", "%d/%m/%Y %H:%M:%S"))
    logout_time = models.DateTimeField(default=datetime.strptime("31/12/9999 23:59:59", "%d/%m/%Y %H:%M:%S"))

