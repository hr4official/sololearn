from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    users = User.get_all_user()
    return render(request,"homepage.html",{'users' : users})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request,"login.html")

""" def userform(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form}) """
    
    