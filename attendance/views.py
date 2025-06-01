from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import TeacherLoginForm
from .models import Attendance, Student
from datetime import date

def index(request):
    return render(request, 'attendance/index.html')

def login_view(request):
    if request.method == "POST":
        form = TeacherLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('attendance:attendance_page')
    else:
        form = TeacherLoginForm()

    return render(request, 'attendance/login.html', {'form': form})

@login_required
def attendance_view(request):
    try:
        student = Student.objects.get(user=request.user)  # get student by linked user
    except Student.DoesNotExist:
        return render(request, 'attendance/attendance.html', {
            'error': "Student record not found for this user."
        })

    attendance_records = Attendance.objects.filter(student=student).order_by('date', 'teacher__user__username')

    grouped_records = {}
    for record in attendance_records:
        date_str = record.date.strftime("%Y-%m-%d")
        if date_str not in grouped_records:
            grouped_records[date_str] = []
        grouped_records[date_str].append({
            'teacher': record.teacher.user.username,
            'status': record.status
        })

    return render(request, 'attendance/attendance.html', {
        'student_name': student.name,
        'attendance_by_date': grouped_records
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('attendance:login.html')
