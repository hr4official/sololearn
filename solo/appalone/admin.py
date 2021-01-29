from django.contrib import admin
from .models import User
# Register your models here.

#registering for reflecting in admin panel
admin.site.register(User)