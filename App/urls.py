from django.urls import path,include
from .views import home,opportunities,email_frontend,email_intern,backend,support,add_message,faq

urlpatterns = [
    # ||===============FRONTEND SECTION================||
    path("",home,name="home"),
    path("opportunities/",opportunities,name="opportunities"),
    path("faq/",faq,name="faq"),
    path("email_frontend",email_frontend,name="email_frontend"),
    path("email_intern",email_intern,name="email_intern"),
    path('user/',include('django.contrib.auth.urls'),name="login"),
    path("support/",support,name='support'),
    path("add_message/",add_message,name='add_message'),

    # ||===============BACKEND SECTION================||
    path('backend/',backend,name='backend')
]
