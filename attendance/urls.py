from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('attendance/', views.attendance_view, name='attendance_page'),
    path('logout/', views.logout_view, name='logout'),
]
