from django.db import models

class SignUp(models.Model):
    visitor_name=models.CharField(max_length=100)
    visitor_phone_number=models.CharField(max_length=15)
    visitor_mail=models.EmailField()
    reason=models.CharField(max_length=100)
    visitor_address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    

    def __str__(self):
        return self.visitor_mail

