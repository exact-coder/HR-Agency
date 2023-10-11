from django.db import models
from django.utils.translation import gettext_lazy as _


# 1) PREVENT DUPLICATE EMAILS
class Registered_email(models.Model):
    email = models.CharField(_("Email"), max_length=50)

    def __str__(self) -> str:
        return self.email
    
# 2) SUPPORT
class Support(models.Model):

    PERSON = {
        ('Employee','Employee'),
        ('Candidate','Candidate'),
    }

    OPTION = {
        ('I lost my account','I lost my account'),
        ('My password does not work','My password does not work'),
        ('Update resume','Update resume'),
        ('Others','Others'),
    }

    SITUATION = {
        ('Done','Done'),
        ('Pending','Pending'),
    }

    terms = models.BooleanField(_("Terms"),"Took Responsibility",default=False)
    message = models.TextField(_("Message"))
    person = models.CharField(_("Person"), max_length=50,choices=PERSON)
    option = models.CharField(_("Option"), max_length=50,choices=OPTION)
    email = models.CharField(_("Email"), max_length=50)
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    Situation = models.CharField(_("Situation"), max_length=50,null=True,blank=True,choices=SITUATION,default='Pending')

    def __str__(self) -> str:
        return self.person

# 3) MESSAGE
class Message(models.Model):
    SITUATION ={
        ('Unread','Unread'),
        ('Read','Read'),
    }
    id = models.IntegerField(_("ID"),primary_key=True)
    email = models.EmailField(_("Email"), max_length=55)
    text = models.TextField(_("Message"))
    created_at = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    Situation = models.CharField(_("Situation"), max_length=50,null=True,blank=True,choices=SITUATION,default='Unread')
