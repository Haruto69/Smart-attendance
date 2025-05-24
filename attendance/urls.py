from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance_view, name='attendance_page'),
]
