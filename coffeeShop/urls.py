from django.contrib import admin
from django.urls import path
from coffeeItems.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('coffee/',Home),
    path('pricing/',Pricing),
    path('register/',SignIn),
    path('login/',LogIn),
]
