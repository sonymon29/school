from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Department

# Create your views here.
def demo(request):
    return render(request,'index2.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('demo')
        else:
            messages.info(request,"invalid credentials")
            return redirect('demo')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"*Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
        
            user.save();
            messages.info(request,"User created succesfully")
            return redirect("login")
        else:
            messages.info(request,"*Password doesnot match.")
            return redirect('register')
    return render(request,'register.html')

@login_required
def form(request):
    if request.method== 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST.get('gender')
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST.get('department')
        # purpose = request.POST['purpose']
        materials = request.POST.get('materials')


    return render(request,'form.html')

def department(request):
    return render(request,)