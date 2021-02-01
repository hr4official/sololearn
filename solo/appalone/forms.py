from django import forms
from .models import User

class UserForm(forms.ModelForm):
    """ name = forms.CharField(label='name',max_length=20)
    surname = forms.CharField(label='name',max_length=20)
    email = forms.EmailField(label='name',max_length=20)
    contact = forms.CharField(label='name',max_length=20)
    image = forms.ImageField(label='name',max_length=20)
     """
    
    class Meta:
        model = User
        fields = ["name","surname","email","contact","image"]
        labels = {"name": "name","surname": "surname","email": "email","contact": "contact","image": "image",}