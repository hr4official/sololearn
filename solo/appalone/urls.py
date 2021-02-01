from django import urls
from django.urls.resolvers import URLPattern
from django.urls import path

from . import views
urlpatterns = [
    #path("form", views.userform, name='form'),
    path("",views.homepage,name="homepage"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
]