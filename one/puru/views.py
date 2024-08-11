from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from puru.models import Uber

# Create your views here.
def home(request):
    obj=Uber.objects.all()
    return render(request,"home.html",{"res":obj})

def logins(request):
    if request.user.is_authenticated:
        
        return redirect('homepage')
    if request.method=="POST":
        uname=request.POST.get("uname")
        passw=request.POST.get('passw')
        print(uname,passw)
        result=authenticate(request,username=uname,password=passw)
        if result:
            login(request,result)
            messages.info(request,"Bro caongratulations you successfully logged in")

            if request.user.is_superuser:
                return redirect("/admin")
            else:
                return redirect("profilepage")
        messages.info(request,"Bro enter correct username and password")
        return redirect("loginpage")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        print(uname,fname,lname,email,passw,cpass)
        if User.objects.filter(username=uname).exists():
            messages.info(request,"Username undhi ra appude try new one !")
            return redirect('registerpage')
        if len(uname)<6:
            messages.info(request,"Bro konchem pedha username enter chey")
            return redirect('registerpage')
        if passw.isalnum():
            messages.info(request,"Bro you should must give one special character")
            return redirect("registerpage")
        
        if len(passw)<8:
            messages.info(request,"Password 8 characters undali ra")
            return redirect('registerpage')
       
        if (cpass!=passw):
            messages.info(request,"Bro both passwords same undali")
            return redirect('registerpage')
        

        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=passw)
        obj.save()
        messages.success(request,"registration completed brooooo..Now Login now")
        return redirect('loginpage')
        
        
        
    return render(request,"register.html")


@login_required(login_url="loginpage")
def profile(request):
    if request.user.is_superuser:
        return redirect("/admin")
    return render(request,"profile.html")

@login_required(login_url="loginpage")
def delete(request,pid):
    if request.user.is_authenticated:
        obj=Uber.objects.get(id=pid)
        obj.delete()
        messages.success(request,"Deletion completed brooooo")
        tot=Uber.objects.all()
        return render(request,"home.html",{"res":tot})
    return render(request,"home.html")

def display(request):
    return render(request,"single.html")

@login_required(login_url="loginpage")
def create(request):
    if request.method=="POST":
        loc=request.POST.get("pname")
        u=request.user.username
        obj=Uber(uname=u,location=loc)
        obj.save()
        return render(request,"create.html",{"res":obj})
    return render(request,"create.html")
        
    return render(request,"create.html")

def logouts(request):
    logout(request)
    
    return redirect("loginpage")
