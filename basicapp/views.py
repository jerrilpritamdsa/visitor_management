from django.shortcuts import render
from .forms import SignUpForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from PIL import Image
import os

                
def email(request):
    if request.method=="GET":
        form=SignUpForm()
    else:
        form=SignUpForm(request.POST)
        if form.is_valid():

            visitor_name=request.POST.get('visitor_name')
            visitor_phone_number=request.POST.get('visitor_phone_number')
            visitor_mail=request.POST.get('visitor_mail')
            reason=request.POST.get('reason')
            visitor_address=request.POST.get('visitor_address')
            contact_person=request.POST.get('contact_person')
            id_number=request.POST.get('id_number')
            
   
            message='Dear '+contact_person+',\nThe mail contains attached photograph of the visitor/candidate\n\n Candidate name : '+visitor_name+"\n Candidate phone number : "+visitor_phone_number+"\n Candidate Email Id : "+visitor_mail+" \n\nIs waiting for "+reason+" purpose, Please confirm the Identity card number once you meet \n Id number : "+id_number
            email=EmailMessage(
                reason,
                message,
                visitor_mail,
                ["SENDER'S_MAIL"]
            )
            pathOut='DOWNLOADED_DRIVE_PATH'
            for f in os.listdir(pathOut):
                if f.endswith('png'):
                    file_path = os.path.join(pathOut, f)
            email.attach_file(str(file_path))
            email.send()
            os.remove(file_path)
    return render(request,'basicapp/signup.html',{'form':form})



