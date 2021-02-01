from django import forms
from django.forms import fields
from django.forms.models import model_to_dict
from .models import User

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ["name","surname","email","contact","image"]
        labels = {"name": "name","surname": "surname","email": "email","contact": "contact","image": "image",}