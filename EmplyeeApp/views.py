from datetime import date
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage

from EmplyeeApp.models import Employee, Department
from EmplyeeApp.serializers import EmployeeSerializer, DepartmentSerializer


# Create your views here.

@csrf_exempt
def departmentApi(request,id =0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many = True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST' :
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data = department_data)
        
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Successfully has been saved', safe=False)
        return JsonResponse('Failed to save', safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(departmentId = department_data['departmentId'])
        department_serializer = DepartmentSerializer(department, department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Successfully has been updated', safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        print('id '+id)
        department = Department.objects.get(departmentId = id)
        department.delete()
        return JsonResponse('Successfully has been deleted',safe=False)

@csrf_exempt
def employeeApi(request,id = 0):
    if request.method == "GET":
        employee_data = Employee.objects.all()
        employee_serialize = EmployeeSerializer(employee_data,many = True)
        return JsonResponse(employee_serialize.data, safe=False)
    elif request.method == "POST":
        employee_data = JSONParser().parse(request)
        employee_serialize = EmployeeSerializer(data = employee_data)

        if employee_serialize.is_valid():
            employee_serialize.save()
            return JsonResponse('Successfully has been saved',safe=False)
        return JsonResponse('Failed to save',safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employeeId = employee_data['employeeId'])
        employee_serialize = EmployeeSerializer(employee, employee_data)
        
        if employee_serialize.is_valid():
            employee_serialize.save()
            return JsonResponse('Successfully has been updated',safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == "DELETE":
        employee = Employee.objects.get(employeeId = id)
        employee.delete()
        return JsonResponse('Successfully has been deleted.', safe=False)
    
@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)