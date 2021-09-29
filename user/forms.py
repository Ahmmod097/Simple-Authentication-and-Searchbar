from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

from . models import UserInfo

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label=('First Name'), max_length=100, min_length=4, required=True, 
                                widget=forms.TextInput(attrs={'cols': 1, 'rows': 2}))
    
    last_name = forms.CharField(label=('Last Name'), max_length=100, min_length=4, required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-group'}))

    address = forms.CharField(label=('Address'), max_length=1000, min_length=4, required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-group'}))

    phone_number = forms.IntegerField(label=('Phone Number'), required=True, 
                                widget=forms.NumberInput(attrs={'class': 'form-group'}))                                                        

    email = forms.EmailField(max_length=50, help_text='Required a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-group'})))

    birthdate = forms.DateField(widget= DateInput)                         
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-group'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-group'}),
                                )
   
   

    class Meta:
        model = User
        fields = ('first_name','last_name', 'address', 'phone_number', 
        'email',  'birthdate', 'password1', 'password2', )


class ChangePassword(forms.Form):
    old_password=forms.CharField(label=_('Old Password'), widget=forms.PasswordInput(),
                                )
    new_password=forms.CharField(label=_('New Password '), widget=forms.PasswordInput(),
                                )
    reenter_password=forms.CharField(label=_('Re-enter Password'), widget=forms.PasswordInput(),
                                )