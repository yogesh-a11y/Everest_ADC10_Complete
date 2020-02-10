from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType
from jobs.models import Jobs
 
# Create your views here.

def user_login(req):
    if req.method=="GET":
        return render(req,'login.html')
    else:
        username=req.POST['username']
        password=req.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(req,user)
            return redirect('jobs_home')
        else:
            return redirect('login') 

def sign_up(req):
    if req.method=="GET":
        return render(req,'sign-up.html')
    else:
        username=req.POST['username']
        password=req.POST['password']
        email=req.POST['email']

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()

        content_type=ContentType.objects.get_for_model(Jobs)

        #view permission
        permission=Permission.objects.get(
            codename='view_jobs',
            content_type=content_type
            
        )

        user.user_permissions.add(permission)
        return redirect('login')

def user_logout(req):
    logout(req)
    return redirect ('login')
    
