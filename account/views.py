from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_page(request):
    if request.method == "GET":
        return render(request,'account/login.html')
    elif request.method == "POST":
        name=request.POST.get('Email');
        password=request.POST.get('password');
        if authenticate(request ,username=name, password=password):
            login(request,user=User.objects.get(username=name))
            return HttpResponse("Auth Successful")
        else:
            return redirect('home')
        return render(request,"base/base.html")
    