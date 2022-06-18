
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dob=request.POST['dob']
        email=request.POST['email']
        user_name=request.POST['username']
        passwd1=request.POST['passwd']
        passwd2=request.POST['cpasswd']
        if passwd1==passwd2:
            if User.objects.filter(username=user_name):
                messages.info(request,'Username already exists')
                return redirect(register)
            elif User.objects.filter(email=email):
                messages.info(request,'Email already exists')
                return redirect(register)
            else:
                user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=passwd1)
                user.save();
                messages.info(request,'User created successfully')
                return redirect('login')
        else:
            print('Password not matching')
        return redirect('/')



    else:
        return render(request, 'register.html')
def login(request): 
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request);
    return redirect('/')