from django.db import models
from Home.models import DoctorProfile, UserProfile, HospitalProfile
from django.contrib.auth.models import User


class Consutation(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete = models.SET_NULL, null = True)
    hospitel = models.ForeignKey(HospitalProfile, on_delete = models.SET_NULL, null = True)
    patient = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    date = models.DateField(auto_now_add = False)
    time = models.TimeField(auto_now_add = False)
    approval = models.BooleanField(default = False)

    def __str__(self):
        return "consultaion on " + str(self.date) + " at " + str(self.time) + "doctor " + str(self.doctor) 




class OrganDonation(models.Model):
    options = (("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-"))
    options1 = (("Kidneys","Kidneys"),("Liver","Liver"),("Lungs","Lungs"),("Heart","Heart"),("Pancreas","Pancreas"),("Intestines","Intestines"),("Hands","Hands"),("Eye","Eye"))

    doner = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null = True)
    organ = models.CharField(max_length = 255, choices=options1)
    Bloodgroup = models.CharField(max_length=255, choices= options)
    HealthPath = models.CharField(max_length = 1000)
    Hospital = models.ForeignKey(HospitalProfile, on_delete = models.SET_NULL, null = True)
    availability = models.BooleanField(default = True)

    def __str__(self):
        return "ORGAN : " + str(self.organ) + "; DONER :" + str(self.doner) + "; Hospital: " + str(self.Hospital)

class Organrequest(models.Model):
    Organ = models.ForeignKey(OrganDonation,on_delete = models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete = models.SET_NULL, null = True)
    hospitel = models.ForeignKey(HospitalProfile, on_delete = models.SET_NULL, null = True)
    patient = models.ForeignKey(UserProfile, on_delete = models.CASCADE, null = True)
    request_status = models.BooleanField(default = True)
    HealthRecord = models.FileField(upload_to="HealthFile",null=True, blank=True)
    is_healthrecord_status = models.BooleanField(default=False)

    def __str__(self):
        return "ORGAN request by" + str(self.doctor) + " Organ " + str(self.Organ) 


class Surgery(models.Model):
    # consultaion = models.ForeignKey(Consutation,on_delete = models.CASCADE)
    organrequest = models.ForeignKey(Organrequest,on_delete = models.CASCADE,null=True)
    patient = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    surgery_date = models.DateField(auto_now_add = False)
    admint_date = models.DateField(auto_now_add = False)
    surgery_status = models.BooleanField(default = True)
    comments_doctor = models.CharField(max_length = 1000, null= True)
    
    def __str__(self):
        return "Surgery Planed for" + str(self.patient) + " Organ " + str(self.organrequest) + "Date " + str(self.surgery_date)

    
