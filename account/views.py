from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_page(request,message=None,type_msg=None):
    if message:
        return render(request,'account/login.html',{"Message":message,"Type":type_msg})
    
    elif request.method == "GET":
        return render(request,'account/login.html',{"Message":message,"Type":type_msg})
    elif request.method == "POST":
        login_or_register = request.POST.get("login_or_signup")
        name=request.POST.get('Email');
        password=request.POST.get('password');
        if authenticate(request ,username=name, password=password):
            login(request,user=User.objects.get(username=name))
            return HttpResponse("Auth Successful")
        else:
            return redirect('home')
def logout_view(request):
    logout(request)
    return redirect('home')
def register(request):
    # return HttpResponse("gfyhdgdshcsdsyuf ewgfyirifgdsivgisdgvisdgvisd")
    if request.method == 'POST':
        email = request.POST.get('Email_sup')
        password = request.POST.get('Pwd2')
        FName = request.POST.get('FName')
        LName = request.POST.get('LName')
        username = email
        user=User.objects.filter(email=email).exists()
        if not user:
            user_c=User.objects.create_user(username=username,email=email,password=password,first_name =FName,last_name = LName)
            user_c.save()
            return login_page(request,"Success! User Created Please login now","success")
        else:
            return login_page(request,"Error! Email already exists please login","danger")