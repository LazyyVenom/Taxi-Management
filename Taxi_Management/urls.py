from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('login',login,name='login'),
    path('login_verify',login_verify,name='login_verify'),
    path('signup',signup,name='signup'),
    path('register',register,name='register'),
]