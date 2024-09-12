from django.http import HttpResponse
from django.shortcuts import redirect
from .models import DoctorProfile, HospitalProfile


#decorator for user redirect...............
def unautenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('Index')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func

# allowed user decorators................
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

#decorators for user wise redirect pages...............
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == None:
            return view_func(request, *args, **kwargs)
            
        if group == 'customer':
            return view_func(request, *args, **kwargs)
        
        if group == 'doctor':
            return redirect('DoctorIndex')

        if group == "hospital":
            return redirect("HospitalIndex")
        
        if group == "admin":
            return redirect("AdminIndex")
              
    return wrapper_function


def DoctorActiveCheck(view_func):
    def warapper_func(request,*args,**kwargs):
        doctor = DoctorProfile.objects.get(user = request.user)
        if doctor.active == True:
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse('<h2 style="text-align: center;">You are Not Autherize to login Please Wait for admin Approval <a href="/SignOut" style="color:red">Back To Home</a></h2>')
        
    return warapper_func

def HospitalActiveCheck(view_func):
    def warapper_func(request,*args,**kwargs):
        doctor = HospitalProfile.objects.get(user = request.user)
        if doctor.active == True:
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse('<h2 style="text-align: center;">You are Not Autherize to login Please Wait for admin Approval <a href="/SignOut" style="color:red">Back To Home</a></h2>')
        
    return warapper_func