from django.shortcuts import render, redirect 
from django.contrib import messages
from Home.models import DoctorProfile, UserProfile, HospitalProfile
from .forms  import ConsultaionAdd, AddOrganDonation, OrganDonationRequest, SurgeyAdd
from .models import Consutation, OrganDonation, Organrequest, Surgery
from django.http import JsonResponse

# Create your views here.

def GetAppoinment(request):
    form = ConsultaionAdd()
    if request.method == "POST":
        form = ConsultaionAdd(request.POST)
        if form.is_valid():
            consultation = form.save()
            consultation.patient = request.user
            consultation.hospitel = consultation.doctor.hospital
            consultation.save()
            messages.info(request,"consultaion Requested.........")
            return redirect("MyAppointments")

    context = {
        "form":form
    }
    return render(request,"getappoinment.html",context)


def MyAppointments(request):
    consultation = Consutation.objects.filter(patient = request.user)

    context = {
        "consultation":consultation
    }
    return render(request,"myappointments.html",context)


def Doctors(request):
    doctor = DoctorProfile.objects.filter(active=True)

    context = {
        "doctor":doctor
    }

    return render(request,"doctors.html",context) 


def OrganDonations(request):
    donation = OrganDonation.objects.filter(doner__user = request.user )

    context = {
        "donation":donation,
        
    }
    return render(request,"donateorgan.html",context)




def Surgeryview(request):
    surgery = Surgery.objects.filter(patient__user = request.user)
    donationrequest = Organrequest.objects.filter(Organ__doner__user = request.user)
    context = {
        "surgery":surgery,
        "donationrequest":donationrequest
    }
    return render(request,"surgery.html",context)


def DoctorConsultaion(request):
    consultation = Consutation.objects.filter(doctor__user = request.user)

    context = {
        "consultation":consultation
    }
    return render(request,"doctorconsultaion.html",context)

def ApproveConsultationrequest(request,pk):
    consutation = Consutation.objects.get(id = pk)
    consutation.approval = True 
    consutation.save()
    messages.info(request,"Request approved...")
    return redirect("DoctorConsultaion")


def DoctorSurgery(request):
    surgey = Surgery.objects.filter(organrequest__doctor__user = request.user)

    context = {
        "surgey":surgey
    }
    return render(request,"doctorsurgery.html",context)


def Addsurgery(request,pk):
    organrequest = Organrequest.objects.get(id = pk)
    form = SurgeyAdd()
    if request.method == "POST":
        form = SurgeyAdd(request.POST)
        if form.is_valid():
            surgery = form.save()
            surgery.organrequest = organrequest
            surgery.save()
            return redirect("Addsurgery", pk= pk)

    context = {
        "form":form
    }
    return render(request,"addsurgery.html",context)

def DoctordonationView(request):
    donation = OrganDonation.objects.all()
    donationrequest = Organrequest.objects.filter(doctor = DoctorProfile.objects.get(user  = request.user))

    context = {
        "donation":donation,
        "donationrequest":donationrequest
    }
    return render(request,"organdoners.html",context)

def OrganDonationAdd(request):
    form = AddOrganDonation()
    users = UserProfile.objects.all()

    if request.method == "POST":
        form = AddOrganDonation(request.POST)
        user = request.POST.get("doner")
        blood = request.POST.get("bloodgroup")
        if form.is_valid():
            donation = form.save()
            donation.doner = UserProfile.objects.get(id = int(user))
            donation.Bloodgroup =  blood
            donation.save() 
            messages.info(request,"Organ Addedd........")
            return redirect("DoctordonationView")
        else:
            messages.info(request,"Organ not Addedd........")
            return redirect("DoctordonationView")
       
           


    context = {
        "form":form,
        "users":users
    }
    return render(request,'addorgan.html',context)


def getbloodgroup(request, donor_id):
    try:
        donor = UserProfile.objects.get(id=donor_id)
        blood_group = donor.Bloodgroup  # Assuming the field name is 'blood_group', adjust it if necessary
        return JsonResponse({'success': True, 'bloodGroup': blood_group})
    except UserProfile.DoesNotExist:
        return JsonResponse({'success': False})


def AddOrganRequets(request):
    form = OrganDonationRequest()
    user = UserProfile.objects.all()

    if request.method == "POST":
        patient_id = request.POST["patientid"]
        profile = UserProfile.objects.get(id = str(patient_id))
       
        form = OrganDonationRequest(request.POST)
        if form.is_valid():
            organrequest = form.save()
            organrequest.patient =  profile
            organrequest.doctor = DoctorProfile.objects.get(user  = request.user)
            organrequest.save()
            messages.info(request,"Organ request Addedd........")
            return redirect("DoctordonationView")
        else:
            messages.info(request,"Something Wrong........")
            return redirect("DoctordonationView")

    context = {
        "form":form,
        "user":user
    }
    return render(request,"adddonationrequest.html",context)


def ConsultationrequestsHospitels(request):
    consultation = Consutation.objects.filter(hospitel__user = request.user )

    context = {
        "consultation":consultation
    }
    return render(request,"counsultaionreq.html",context)


def SurgeryHospital(request):
    hospital = HospitalProfile.objects.get(user = request.user)
    print(hospital)
    surgery = Surgery.objects.filter(organrequest__doctor__hospital = hospital)
    print(surgery)
    print(request.user)
    context = {
        "surgery":surgery
    }
    return render(request,"surgeryHospital.html",context)

def OrganDonationHospital(request):
    donation = OrganDonation.objects.all()
    context = {
        "donation":donation
    }
    return render(request,"donnershospital.html",context)

def UploadRecord(request,pk):
    donerrequest = Organrequest.objects.get(id = pk)
    if request.method == "POST":
        record = request.FILES['record']
        donerrequest.HealthRecord = record
        donerrequest.is_healthrecord_status = True
        donerrequest.save()
        messages.info(request,"Health Record Uploaded....")
        return redirect("Surgeryview")
    return redirect("Surgeryview")
