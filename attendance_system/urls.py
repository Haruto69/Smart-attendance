from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),    
    path('', include('attendance.urls')),  # Redirect root to login
]   