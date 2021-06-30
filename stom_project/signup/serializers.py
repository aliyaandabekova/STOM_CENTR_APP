from rest_framework import serializers
from .models import *

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class DoctorDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDay
        fields = '__all__'
