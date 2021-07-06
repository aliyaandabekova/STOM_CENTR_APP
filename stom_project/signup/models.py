from django.contrib.auth.models import User
from django.db import models

class Day(models.Model):
    name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name


class DoctorDay(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    status = models.CharField(choices=(
        ('free','free'),
        ('reserved','reserved')
    ),max_length=10,default='free')

class Order(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='clients')
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctors')
    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
