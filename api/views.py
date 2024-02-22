from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from datetime import date

from main import models
from . import serializer


@api_view(['POST'])
def staff_create(request):
    f_name = request.data.get('f_name')
    l_name = request.data.get('l_name')
    if f_name and l_name:
        models.Employee.objects.create(
            f_name = f_name,
            l_name = l_name,
        )
        return Response({'status':HTTP_200_OK})
    return Response({'status':HTTP_400_BAD_REQUEST})


@api_view(['GET'])
def staff_list(request):
    employee = models.Employee.objects.all()
    ser = serializer.EmployeeSerializers(employee, many=True)
    return Response(ser.data)


@api_view(['POST'])
def attendance_create(request, id):
    employee = models.Employee.objects.get(id = id)
    if employee:
        models.Attendance.objects.create(
            employee = employee
        )
        return Response({'status':HTTP_200_OK})
    return Response({'status':HTTP_400_BAD_REQUEST})


@api_view(['GET'])
def attendance_day(request):
    attendance = models.Attendance.objects.filter(date_time__day = date.today())
    ser = serializer.AttendanceSerializers(attendance)
    return Response(ser.data)


