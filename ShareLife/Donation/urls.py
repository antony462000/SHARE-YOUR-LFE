from django.urls import path 
from .import views

urlpatterns = [
    path("GetAppoinment",views.GetAppoinment,name="GetAppoinment"),
    path("MyAppointments",views.MyAppointments,name="MyAppointments"),
    path("Doctors",views.Doctors,name="Doctors"),
    path("OrganDonations",views.OrganDonations,name="OrganDonations"),
    path("Surgeryview",views.Surgeryview,name="Surgeryview"),
    path("DoctorConsultaion",views.DoctorConsultaion,name="DoctorConsultaion"),
    path("DoctorSurgery",views.DoctorSurgery,name="DoctorSurgery"),
    path("OrganDonationAdd",views.OrganDonationAdd,name="OrganDonationAdd"),
    path("DoctordonationView",views.DoctordonationView,name="DoctordonationView"),
    path("ApproveConsultationrequest/<int:pk>",views.ApproveConsultationrequest,name="ApproveConsultationrequest"),
    path("AddOrganRequets",views.AddOrganRequets,name="AddOrganRequets"),
    path("ConsultationrequestsHospitels",views.ConsultationrequestsHospitels,name="ConsultationrequestsHospitels"),
    path("Addsurgery/<int:pk>",views.Addsurgery,name="Addsurgery"),
    path("SurgeryHospital",views.SurgeryHospital,name="SurgeryHospital"),
    path("OrganDonationHospital",views.OrganDonationHospital,name="OrganDonationHospital"),
    path('getbloodgroup/<int:donor_id>/', views.getbloodgroup, name='getbloodgroup'),
    path("UploadRecord/<int:pk>",views.UploadRecord,name="UploadRecord"),

    
]       
  
