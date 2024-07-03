from rest_framework import serializers
from . import models


class EmployeeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Employee
        fields = '__all__'
        
        
class AttendanceSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Attendance
        fields = '__all__'

