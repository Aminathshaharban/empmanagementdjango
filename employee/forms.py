from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter the Name"}))
    position=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter position"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter age"}))
    department=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter department"}))
    phone_no=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone number"}))
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter salary"}))


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form_control","placeholder":"Enter username"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form_control","placeholder":"Enter password"}))
    

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        