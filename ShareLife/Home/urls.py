from django.urls import path 
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path('SignIn',views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("HospitalSignUp",views.HospitalSignUp,name="HospitalSignUp"),
    path("DoctorSignUp",views.DoctorSignUp,name="DoctorSignUp"),
    path("DoctorIndex",views.DoctorIndex,name="DoctorIndex"),
    path("HospitalIndex",views.HospitalIndex,name="HospitalIndex"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("ApproveDoctor/<int:pk>",views.ApproveDoctor,name="ApproveDoctor"),
    path("ApproveHospital/<int:pk>",views.ApproveHospital,name="ApproveHospital"),
   
]       
  
