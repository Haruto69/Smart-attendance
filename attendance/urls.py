from django.urls import path
from django.contrib import admin
from . import views

app_name = 'attendance'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance_view, name='attendance_page'),
]
