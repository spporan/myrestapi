from django.db import models
from django.db.models import fields
from rest_framework import serializers
from EmplyeeApp.models import Employee,Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employeeId','employeeName','dateOfJoining','departmentName','photoFileUrl')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('departmentId','departmentName')