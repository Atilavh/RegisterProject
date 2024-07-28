from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن همراه')
    confirm_code = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'کابر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.fullname} {self.email}'
