from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, DoctorProfile, HospitalProfile
from django.forms import ModelForm, Select, Textarea, TextInput
from datetime import date

today = date.today()

class UserProfileAddForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["last_name","date_of_birth","Bloodgroup","Address","district","state","phone","profile_pic"]

        widgets = {
            "phone":TextInput(attrs={"type":"tel","pattern":"[0-9]{10,12}", "title":"Please enter the mobile number with specific country code(India : 0091xxxxxxxxxx, etc..)"}),
            "date_of_birth":TextInput(attrs={"type":"date","max":today}),
        }

class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]


class DoctorProfileAddForm(ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ["last_name","Specilisation","Address","district","state","phone","profile_pic","hospital"]

        widgets = {
            "phone":TextInput(attrs={"type":"tel","pattern":"[0-9]{10,12}", "title":"Please enter the mobile number with specific country code(India : 0091xxxxxxxxxx, etc..)"}),
            
        }


class HospitalProfileAddForm(ModelForm):
    class Meta:
        model = HospitalProfile
        fields = ["name","Address","district","state","phone","profile_pic"]

        widgets = {
            "phone":TextInput(attrs={"type":"tel","pattern":"[0-9]{10,12}", "title":"Please enter the mobile number with specific country code(India : 0091xxxxxxxxxx, etc..)"}),
            
        }


