from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee, UserDataForm

class EmployeeForm(forms.ModelForm):
    class Meta:  
        model = Employee
        fields = "__all__"
    
class NewUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        # labels = {'email': 'Email' }
            



