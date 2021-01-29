from django.shortcuts import render
from .models import User
# Create your views here.
def homepage(request):
    users = User.get_all_user()
    return render(request,"homepage.html",{'users' : users})

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")