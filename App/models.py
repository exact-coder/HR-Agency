from django.db import models
from django.utils.translation import gettext_lazy as _


# 1) PREVENT DUPLICATE EMAILS
class Registered_email(models.Model):
    email = models.CharField(_("Email"), max_length=50)

    def __str__(self) -> str:
        return self.email
        
    class Meta:
        verbose_name_plural ="Registered_email"
    
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
        
    class Meta:
        verbose_name_plural ="Support"

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
        
    class Meta:
        verbose_name_plural ="Messages"

# 4) NODEPAD
class Notepad(models.Model):
    id = models.IntegerField(_("ID"),primary_key=True)
    title = models.CharField(_("Title"), max_length=80)
    text = models.TextField(_("Text"))

    def __str__(self) -> str:
        return self.title
        
    class Meta:
        verbose_name_plural ="Notepad"
    
#  5) JOB VACANCIES
class Vacancies(models.Model):
    id = models.IntegerField(_("ID"),primary_key=True)
    frontend = models.CharField(_("Frontend"), max_length=150)
    backend = models.CharField(_("Backend"), max_length=150)
    fullstack = models.CharField(_("Fullstack"), max_length=150)
    intern = models.CharField(_("Intern"), max_length=150)
    def __str__(self) -> str:
        return self.frontend
        
    class Meta:
        verbose_name_plural ="Vacancies"
    
# 6) COUNTDOWN
class Countdown(models.Model):
    id = models.IntegerField(_("ID"),primary_key=True)
    timer = models.CharField(_("Timer"), max_length=100)
        
    class Meta:
        verbose_name_plural ="Countdown"

# WAITING LIST

JOB = (
    ('Frontend','Frontend'),
    ('Backend','Backend'),
    ('Fullstack','Fullstack'),
    ('Intern','Intern'),
)

SITUATION ={
    ('Read','Read'),
    ('Unread','Unread'),
}

class Waiting(models.Model):
    job = models.CharField(_("Job Title"), max_length=150, choices=JOB)
    email = models.EmailField(_("Email"), max_length=254)
    message = models.TextField(_("Message"))
    Situation = models.CharField(_("Situation"), max_length=50,null=True,blank=True,choices=SITUATION,default='Unread')
    created_at = models.DateTimeField(_("Created At"), auto_now=False, auto_now_add=True)
    profile_document = models.FileField(_("Resume"), upload_to='resume')
    company_note = models.TextField(_("Company Note"),null=True,blank=True)

    def __str__(self) -> str:
        return self.job
    
    class Meta:
        verbose_name_plural ="Waiting"

