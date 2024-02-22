from typing import Iterable
from django.db import models


class Employee(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.f_name} {self.l_name}'
    
    
class Attendance(models.Model):
    come = models.BooleanField(default=False)
    attendance_date = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.employee.f_name} {self.employee.l_name}'
    
    def save(self, *args, **kwargs) -> None:
        if not self.pk:
            self.come = not self.come
        return super(Attendance, self).save(*args, **kwargs)
    
    
    
