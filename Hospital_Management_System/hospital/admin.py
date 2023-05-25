from django.contrib import admin
from .models import Doctor,Patience,Appointment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patience)
admin.site.register(Appointment)
