from __future__ import unicode_literals

from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

Status_choices=(('Dr','Doctor'),
                ('In','Institution'),
                ('Mr/Ms','user'))


class User(AbstractUser):
    mobile = models.IntegerField(blank=True, null=True)
    login = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True, default='',null=True)
    status = models.CharField(max_length=50, choices=Status_choices, default='user')
    name = models.CharField(max_length=50, blank=True, default='')
    profile_image = models.ImageField(upload_to="uploads/images/", blank=True,default='')

    def __str__(self):
        return self.username

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=125, blank=True)
    bio = models.CharField(max_length=10000, blank=True, default='',null=True)
    consultation_location = models.CharField(max_length=125, blank=True, default='')
    consultation_time = models.DurationField(blank=True,null=True,default=timedelta())

    def __str__(self):
        return self.user.username


class Qualification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=120, blank=True, default='')


class Achievements(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True, default='')
    url = models.URLField(blank=True, default='')
    #a_image = models.ImageField(upload_to="uploads/images/", blank=True)


class Health_status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    disease = models.CharField(max_length=120, blank=True, default='')


class Rating(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, default=2)
    score = models.IntegerField(blank=True, default=2)



