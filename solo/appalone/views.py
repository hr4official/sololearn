from django.shortcuts import render
from .models import User
from .forms import UserForm
# Create your views here.
def homepage(request):
    users = User.get_all_user()
    return render(request,"homepage.html",{'users' : users})

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

def userform(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'login.html', {'form': form})
    
    