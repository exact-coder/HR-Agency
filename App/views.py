from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader


# Create your views here.

def home(request):
    return render(request,"home.html")

def opportunities(request):
    return render(request,"opportunities.html")

def email_frontend(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        
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