from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(models.Model):
    options = (("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-"))
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now_add = False)
    Bloodgroup = models.CharField(max_length=255, choices= options)
    Address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to="profilepic")
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True)

    def __str__(self):
        return str(self.user.first_name) + str(self.last_name)
   


    
class HospitalProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    profile_pic = models.FileField(upload_to="profilepic")
    active = models.BooleanField(default = False)


    def __str__(self):
        return str(self.name) + " Hospital"
    

class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    last_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    Specilisation = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to="profilepic")
    active = models.BooleanField(default = False)
    hospital = models.ForeignKey(HospitalProfile,on_delete=models.CASCADE,null=True, blank=True) 
    

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.Specilisation) + " of " + str(self.hospital)
