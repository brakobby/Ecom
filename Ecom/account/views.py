from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Registration
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def accountLogin(request):
    if request.method =='POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conPassword = request.POST['confirm_password']

        if password != conPassword:
            messages.error(request, "Password do not match")
            return redirect('register')
        
        if Registration.objects.filter(username = username).exists():
            messages.error(request, "username already exists")
            return redirect('register')
        
        hashed_password = make_password(password)

        userAccount = Registration.objects.create(
            fullname = fullname,
            username = username,
            email = email,
            password = hashed_password
        )

        userAccount.save()
        messages.success(request, "Account has been created successfully")
        return redirect('login')
    
    return render(request, 'login/registration.html')


def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            userAccount = Registration.objects.get(username=username, password=password)
            messages.success(request, f"Welcome {userAccount.fullname}!")
            return render(request, 'login/accounts.html')
        
        except Registration.DoesNotExist:
            messages.error(request, 'Invalid username or password')

            return redirect('login')
    return render(request, 'login/accounts.html')