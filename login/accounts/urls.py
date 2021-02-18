from django.urls  import path
from . import views
urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    #path('login/',views.),
    path('register/',views.registerView,name="register_url"),
   
]