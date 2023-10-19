from django.urls import path,include
from .views import home,opportunities,email_frontend,email_intern,backend,support,add_message,faq,edit_notepad,edit_vacancies,edit_countdown,waiting

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
    path("waiting/",waiting,name='waiting'),

    # ||===============BACKEND SECTION================||
    path('backend/',backend,name='backend'),
    path('edit_notepad/',edit_notepad,name='edit_notepad'),
    path('edit_vacancies/',edit_vacancies,name='edit_vacancies'),
    path('edit_countdown/',edit_countdown,name='edit_countdown'),
]
