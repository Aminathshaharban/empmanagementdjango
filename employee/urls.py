from django.urls import path
from .views import *


urlpatterns =[
    path('reg',RegView.as_view(),name='userreg'),
    path('landing',LandingView.as_view(),name='landing'),
    path('dashboard',DashboardView.as_view(),name='dashboard'),
    path('add',AddEmployeeView.as_view(),name='addemployee'),
    path('delete/<int:id>',DeleteEmployeeView.as_view(),name='deleteemployee'),
    path('edit/<int:id>',EditEmployeeView.as_view(),name='editemployee'),
    
]