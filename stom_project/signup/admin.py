from django.contrib import admin
from .models import *

admin.site.register(Day)

class DayDoctorDisplay(admin.ModelAdmin):
    list_display = ['doctor','day']
admin.site.register(DoctorDay,DayDoctorDisplay)

