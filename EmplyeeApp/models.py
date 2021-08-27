from django.db import models
from datetime import datetime
# Create your models here.

class Department(models.Model):

    departmentId = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=200)

class Employee(models.Model):

    employeeId = models.AutoField(primary_key=True)
    employeeName = models.CharField(max_length=200)
    dateOfJoining = models.DateField(default=datetime.now,blank=True)
    departmentName = models.CharField(max_length=200)
    photoFileUrl = models.FileField(upload_to='image')