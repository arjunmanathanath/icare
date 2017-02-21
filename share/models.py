from django.db import models
from django.conf import settings
from userauth.models import Doctor

# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank =True)
    time = models.DateTimeField(null=True, blank =True)
    sentiment = models.CharField(max_length=50,null=True, blank =True,default='neutral')

class Sclassifier(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50,null=True, blank =True)
    i_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    d_id = models.ForeignKey(Doctor,models.CASCADE,)

class Templog(models.Model):
    experience = models.OneToOneField(Experience, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=50,null=True, blank =True)
    institution = models.CharField(max_length=50,null=True, blank =True)
    place = models.CharField(max_length=50,null=True, blank =True)
    regno = models.IntegerField(null=True, blank =True,default=0)







