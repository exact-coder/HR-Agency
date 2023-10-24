from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Registered_email,Support,Message,Notepad,Vacancies,Countdown,Waiting
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


# Create your views here.
# ||================= FRONTEND SECTION ================||

def home(request):
    return render(request,"home.html")

def opportunities(request):
    myJob = Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    return render(request,"opportunities.html",{'vacancies':myJob,'countdowns': myCountdown})

def faq(request):
    return render(request,"faq.html")

# Function to send frontend from
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

# Function to send intern form
def email_intern(request):
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
                "Intern - Candidate",message,
                "Intern Opportunity",['hasanakash799@gmail.com']
            )
            email.content_subtype = "html"
            file = request.FILES['file']
            email.attach(file.name,file.read(),file.content_type)
            email.send()
            messages.success(request,"Successfully Send. Send a copy to your email also!!")
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/opportunities")


# Support
def support(request):
    if request.method == 'POST':

        # check if email exist in DB
        email = request.POST['email']

        # If Candidate or User not exists, deny submit
        if not Registered_email.objects.filter(email=email).exists() and not User.objects.filter(email=email).exists():
            messages.warning(request, 'Email address not Registered !')
            return HttpResponseRedirect('/support')

        # if situation = 'Pending' deny new request
        if Support.objects.filter(email=email, Situation = "Pending").exists():
            messages.info(request,".") #Argument inside the message can't be empty(It's because i put a dot (.))
            return HttpResponseRedirect('/support')
        else:
            support = Support()

            message = request.POST.get('message')
            terms = request.POST.get('terms')
            person = request.POST.get('person')
            option = request.POST.get('option')
            email = request.POST.get('email')

            support.message = message
            support.terms = terms
            support.person = person
            support.option = option
            support.email = email

            support.save()
            messages.success(request, 'We will review your request !')
            if not request.user.is_authenticated:
                return HttpResponseRedirect('/')
            else:
                messages.success(request, 'We will review your request !')
                return HttpResponseRedirect('/backend')
            
    else:
        myCountdown = Countdown.objects.all()
        return render(request,"support.html",{'countdowns': myCountdown})

# MESSAGE
def add_message(request):
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('message'):
            message = Message()
            message.email = request.POST.get('email')
            message.text = request.POST.get('message')
            message.save()
            messages.success(request, 'Message send successfully !')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"All field are required !!")
            return HttpResponseRedirect('/')
    else:
        return render(request,"home.html")
    
def waiting(request):
    if request.method == "POST":
        email = request.POST['email']

        if Waiting.objects.filter(email=email).exists():
            messages.warning(request, ".")
            return HttpResponseRedirect('/waiting')
        else:
            file = request.FILES['profile']
            attach = FileSystemStorage()
            profile_doc = attach.save(file.name, file)

            waitingdata = Waiting(
                job = request.POST.get('job'),
                email = request.POST.get('email'),
                profile_document = profile_doc,
                message = request.POST.get('message')
            )
            waitingdata.save()
            messages.success(request, 'Successfully Registered !')
            return HttpResponseRedirect('/')
    else:
        myCountdown = Countdown.objects.all()
        return render(request, 'wating_list.html',{'countdowns':myCountdown})


# ||================= BACKEND SECTION ================||

# Backend homepage
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def backend(request):
    total = Registered_email.objects.all().count()
    myNote = Notepad.objects.all()
    myjobs = Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    return render(request, 'backend.html', {'count': total,'notepads': myNote, 'vacancies':myjobs,'countdowns': myCountdown})

# Nodepad
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_notepad(request):
    if request.method == "POST":
        notepad = Notepad.objects.get(id= request.POST.get('id'))
        if notepad != None:
            notepad.title = request.POST.get('title')
            notepad.text = request.POST.get('text')
            notepad.save()
            messages.success(request, 'Notepad updated successfully !')
            return HttpResponseRedirect('/backend')

# Vacancies
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_vacancies(request):
    if request.method == "POST":
        vacancy = Vacancies.objects.get(id = request.POST.get('id'))
        if vacancy != None:
            vacancy.frontend = request.POST.get('frontend')
            vacancy.backend = request.POST.get('backend')
            vacancy.fullstack = request.POST.get('fullstack')
            vacancy.intern = request.POST.get('intern')
            vacancy.save()
            messages.success(request, 'Job vacancies updated successfully !')
            return HttpResponseRedirect('/backend')
        
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url="login")
def edit_countdown(request):
    if request.method == "POST":
        countdown = Countdown.objects.get(id=request.POST.get('id'))
        if countdown != None:
            countdown.timer = request.POST.get('timer')
            countdown.save()
            messages.success(request, 'Countdown updated successfully !')
            return HttpResponseRedirect('/backend')
        
