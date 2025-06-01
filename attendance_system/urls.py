from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),    
    path('', lambda request: redirect('attendance:login')),  # Redirect root to login
]
