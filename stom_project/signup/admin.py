from django.contrib import admin
from .models import *

admin.site.register(Day)

class DayDoctorDisplay(admin.ModelAdmin):
    list_display = ['doctor','day']
admin.site.register(DoctorDay,DayDoctorDisplay)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['day','doctor','date_created','client']
admin.site.register(Order,OrderAdmin)


