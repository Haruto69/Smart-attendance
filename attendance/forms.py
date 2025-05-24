from django import forms
from django.contrib.auth.forms import AuthenticationForm

class TeacherLoginForm(AuthenticationForm):
    # You can add extra fields if needed (e.g., remember me)
    pass
