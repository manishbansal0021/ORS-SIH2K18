from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def user_dashboard(request):
    pass

def login_view(request):
    pass
def logout_view(request):
    logout(request)
    pass



def registration_view(request):
    pass

def hospital_selection(request):
    pass



def confirmation(request):
    pass




