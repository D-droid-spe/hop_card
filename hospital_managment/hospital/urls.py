from django.contrib import admin
from django.urls import path
from django import contrib
from django import urls
from . import views
from hospital.views import About,Home,contact,Login,logout_admin,add_doctor_info

urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',contact,name='contact'),
    path('admin_login/',Login,name='login'),
    path('logout/',logout_admin,name='logout'),
    path('patient_illness_info/', views.patient_illness_info, name='patient_illness_info'),
     path('doctors_form.html/',add_doctor_info, name='doctors_form'),



    


   
]
