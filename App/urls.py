from django.urls import path,include
from .views import home,opportunities,email_frontend,backend,support,add_message

urlpatterns = [
    # ||===============FRONTEND SECTION================||
    path("",home,name="home"),
    path("opportunities/",opportunities,name="opportunities"),
    path("email_frontend/",email_frontend,name="email_frontend"),
    path('user/',include('django.contrib.auth.urls'),name="login"),
    path("support/",support,name='support'),
    path("add_message/",add_message,name='add_message'),

    # ||===============BACKEND SECTION================||
    path('backend/',backend,name='backend')
]
