from django.shortcuts import render,redirect
from django.views import View
from .forms import LoginForm,RegForm,EmployeeForm
from .models import Employee
from django.contrib.auth import authenticate, login

# Create your views here.

class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")


class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"userlogin.html",{"form":form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
           uname=formdata.cleaned_data.get('username')
           pswd=formdata.cleaned_data.get('password')
           user=authenticate(request,username=uname,password=pswd)
           login(request,user)
           if user:
               return redirect('landing')
           else:
               return redirect('userlog')
        return render(request,'userlogin.html',{"form":formdata})

   
    
class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"userreg.html",{"form":form})
    def post(self,request):
        formdata=RegForm(data=request.POST)
        if formdata.is_valid():
           formdata.save()
           return redirect('userlog')
        return render(request,'userreg.html',{"form":formdata})

    
class DashboardView(View):
    def get(self,request):
        print(self.request.user)
        print(self.request.user.is_staff)
        data=Employee.objects.all()
        return render(request,"dashboard.html",{"data":data})
    
class AddEmployeeView(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,'addemployee.html',{"form":form})
    def post(self,request):
        formdata=EmployeeForm(data=request.POST)
        if formdata.is_valid():
            # print(formdata.cleaned_data)
            # title=formdata.cleaned_data.get('id')
            name=formdata.cleaned_data.get('name')
            pos=formdata.cleaned_data.get('position')
            age=formdata.cleaned_data.get('age')
            phn=formdata.cleaned_data.get('phone_no')
            dept=formdata.cleaned_data.get('department')
            salary=formdata.cleaned_data.get('salary')
            Employee.objects.create(name=name,position=pos,age=age,phone_no=phn,department=dept,salary=salary)
            return redirect('dashboard')
        return render(request,'addemployee.html',{"form":formdata})
    
    
class DeleteEmployeeView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        print(tid)
        employee=Employee.objects.get(id=tid)
        employee.delete()
        return redirect('dashboard')
    

class EditEmployeeView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        employee=Employee.objects.get(id=tid)
        form=EmployeeForm(initial={"name":employee.name,"position":employee.position,"age":employee.age,"phone_no":employee.phone_no,"department":employee.department,"salary":employee.salary})
        return render(request,"editemployee.html",{"form":form})

    def post(self,request,**kwargs):
        formdata=EmployeeForm(data=request.POST)
        tid=kwargs.get('id')
        employee=Employee.objects.get(id=tid)
        if formdata.is_valid():
            # id=formdata.cleaned_data.get('id')
            name=formdata.cleaned_data.get('name')
            pos=formdata.cleaned_data.get('position')
            age=formdata.cleaned_data.get('age')
            phn_no=formdata.cleaned_data.get('phone_no')
            dept=formdata.cleaned_data.get('department')
            salary=formdata.cleaned_data.get('salary')
            # Employee.id=id
            employee.name=name
            employee.position=pos
            employee.age=age
            employee.phone_no=phn_no
            employee.department=dept
            employee.salary=salary
            employee.save()
            return redirect('dashboard')
        return render(request,"editemployee.html",{"form":formdata})




