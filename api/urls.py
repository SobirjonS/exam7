from django.urls import path
from . import views

urlpatterns = [
    path('staff-list', views.staff_list),
    path('staff-create', views.staff_create),
    path('attendance-create/<int:id>', views.attendance_create),
    path('attendance-day', views.attendance_day),    
    path('attendance-week', views.attendance_week),    
    path('attendance-month', views.attendance_month),    
]
