from django.contrib import admin
from .models import *
from Home.models import *

# Register your models here.
admin.site.register(OrganDonation)
admin.site.register(Consutation)
admin.site.register(Organrequest)
admin.site.register(Surgery)
admin.site.register(DoctorProfile)
admin.site.register(HospitalProfile)
admin.site.register(UserProfile)



