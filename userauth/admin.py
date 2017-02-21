from django.contrib import admin

# Register your models here.
from userauth.models import User, Doctor, Qualification, Achievements, Health_status, Rating

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Qualification)
admin.site.register(Achievements)
admin.site.register(Health_status)
admin.site.register(Rating)
