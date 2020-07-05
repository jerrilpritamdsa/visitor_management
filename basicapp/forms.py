from django import forms
from .models import *

from camera_imagefield import CameraImageField

class SignUpForm(forms.ModelForm):
    visitor_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"forms-control"}))
    visitor_phone_number=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':"forms-control"}))
    visitor_mail=forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':"form-control",'id':"clientemail"}))
    reason=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"forms-control"}))
    visitor_address = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"forms-control"}))
    contact_person = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"forms-control"}))
    id_number = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':"forms-control"}))


    class Meta:
        model=SignUp
        fields=['visitor_name','visitor_phone_number','visitor_mail','reason','visitor_address','contact_person','id_number']

    
    

