from django.urls import path
from .views import home,opportunities,email_frontend

urlpatterns = [
    path("",home,name="home"),
    path("opportunities/",opportunities,name="opportunities"),
    path("email_frontend",email_frontend,name="email_frontend"),
]
