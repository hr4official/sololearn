from django.db import models

# Create your models here.

#database 
class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=10)
    image = models.ImageField(max_length=10)
    
    @staticmethod
    def get_all_user():
        return User.objects.all()