from django.urls import path,include
from .views import home,opportunities,email_frontend,backend

urlpatterns = [
    # ||===============FRONTEND SECTION================||
    path("",home,name="home"),
    path("opportunities/",opportunities,name="opportunities"),
    path("email_frontend/",email_frontend,name="email_frontend"),
    path('user/',include('django.contrib.auth.urls'),name="login"),

    # ||===============BACKEND SECTION================||
    path('backend/',backend,name='backend')
]
