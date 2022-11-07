# visitor_management
This is a Visitor Management app that can be used at front dest of any insttitutions for when the visitor comes to visit a personal for given reasons.

The visitor will have to enter his details on the front desk system such as name, phone number, reason and take the picture through the webcam.
The visitor management will store the visitor details and send a drafted mail to the personnel along with the attached photo of that visitor so that he/she/they can confirm the identity of said visitor.

This app has been made with django framework and it requires crispy_forms for form formats

In the settings.py file of form_to_mail, Replace HOST_EMAIL_ID with the email id and HOST_EMAIL_ID_PASSWORD to the password of the said email, 
In the views.py file of basicapp,Replace SENDER'S_MAIL to the institute personnel mail id and  Replace DOWNLOADED_DRIVE_PATH to the system downloads path for eg:'C:\Users\USER\Downloads' 
