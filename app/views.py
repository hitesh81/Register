from django.shortcuts import render, HttpResponseRedirect, reverse
from random import randint
from .models import *
import sys
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')


def registertion(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    password=request.POST['pass']
    cpassword=request.POST['cpass']

    user=registions.objects.filter(email=email)
    if user:
        message = "This user is alery exist"
        return render(request, "register.html", {'message': message})
    else:
        if cpassword == password:
            newuser = registions.objects.create(firstname=fname,lastname=lname,email=email, password=password)
            return render(request, "index.html")

def login(request):
    email=request.POST['email']
    password=request.POST['pass']

    user =registions.objects.filter(email=email)
    if user[0].email == email and user[0].password == password:
        message = "login successfuly"
        s =registions.objects.all()
        return render(request,"success.html", {'s':s})