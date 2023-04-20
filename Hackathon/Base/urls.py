from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    # path('', views.home, name="home"),
    path('hackathon/', views.HackathonPost,name="hackathon"),
    path('hackathon/list/', views.Hackathonget, name="hackathonget"),
    path('registration/all/', views.Registrationget, name="registrationget"),
    path("register/", views.RegistrationPost, name="RegistrationPost"),
    path('user/hackathon/<str:username>/',views.GetUserHackathon, name="GetUserHackathon"),
    path('user/createsubmission/<str:username>/<str:hackathon>/',views.create_submission, name="contact"),
    path('user/submission/<str:username>/' ,views.Submissionget, name="Submissionget"),
    
    
    
]
