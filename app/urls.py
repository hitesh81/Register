from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
         path('', views.index, name="login"),
         path('login', views.login, name='login'),
         path('register', views.register, name='register'),
         path('registertion', views.registertion, name='registertion'),
         path('success', views.success, name='success'),
]
