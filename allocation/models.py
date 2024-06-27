# models.py
from django.db import *

class Group(models.Model):
    group_id = models.CharField(max_length=10)
    members = models.IntegerField()
    gender = models.CharField(max_length=20)

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    gender = models.CharField(max_length=20)