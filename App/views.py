from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Registered_email
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control



# Create your views here.
# ||================= FRONTEND SECTION ================||

def home(request):
    return render(request,"home.html")

def opportunities(request):
    return render(request,"opportunities.html")

def email_frontend(request):
    if request.method == "POST":

        email = request.POST['email']
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request,"We already have your resume in our DB")
            return HttpResponseRedirect('/opportunities')
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            skills = request.POST.get('skills')

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()
            # ===================
            
            template = loader.get_template('resume_form.txt')

            context = {'name':name,'age':age,'email':email,'phone':phone,'address':address,'experience':experience,'skills':skills}

            message = template.render(context)

            """ email = EmailMultiAlternatives(
                "Frontend - Candidate",message,
                "Frontend Opportunity",['hasanakash799@gmail.com',email]
            ) """
            email = EmailMultiAlternatives(
                "Frontend - Candidate",message,
                "Frontend Opportunity",['hasanakash799@gmail.com']
            )
            email.content_subtype = "html"
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            messages.success(request,"Successfully Send. Send a copy to your email also!!")
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/opportunities")


# ||================= BACKEND SECTION ================||

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, 'backend.html')

