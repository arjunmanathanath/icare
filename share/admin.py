from django.contrib import admin

# Register your models here.
from share.models import Experience,Templog

admin.site.register(Experience)
admin.site.register(Templog)