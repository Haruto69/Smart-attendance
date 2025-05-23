from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TeacherLoginForm
from .models import Attendance
from datetime import date

# Teacher Login View
def login_view(request):
    if request.method == "POST":
        form = TeacherLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            teacher = authenticate(request, username=username, password=password)
            if teacher is not None:
                login(request, teacher)
                return redirect('attendance:attendance_page')  # Redirect to attendance page
    else:
        form = TeacherLoginForm()

    return render(request, 'attendance/login.html', {'form': form})

# Attendance View - View attendance data
@login_required
def attendance_view(request):
    # Fetch today's attendance records
    today = date.today()
    attendance_records = Attendance.objects.filter(date=today)

    return render(request, 'attendance/attendance.html', {'attendance_records': attendance_records, 'date': today})

