from django import forms
from .models import User

class UserForm(forms.ModelForm):   
    class Meta:
        model = User
        fields = ["name","surname","email","contact","image"]
        labels = {"name": "name","surname": "surname","email": "email","contact": "contact","image": "image",}