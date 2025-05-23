from django.db import models
from django.contrib.auth.models import User

# Model for Teacher login (using Django's built-in User model)
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add additional fields if required, e.g., subject or department.
    
    def __str__(self):
        return self.user.username

# Model for Student Attendance
class Attendance(models.Model):
    student_id = models.CharField(max_length=50)
    date = models.DateField()
    status = models.BooleanField(default=False)  # True = Present, False = Absent
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_id} - {self.date} - {'Present' if self.status else 'Absent'}"

