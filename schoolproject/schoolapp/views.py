from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Form as FormModel


# Create your views here.
def demo(request):
    return render(request,'index.html')

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


class Form(forms.ModelForm):
    materials = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Debt Notebook', 'Debt Notebook'),
            ('Exam Papers', 'Exam Papers'),
            ('Pen', 'Pen'),
            # Add more choices here
        ],
    )

    class Meta:
        model = FormModel
        fields = ['name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'department', 'purpose', 'materials']

@login_required
def form_view(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Order Confirmed Successfully.')
            return render(request, 'form.html')
        else:
            messages.error(request, 'There was an error in your form.')
            return render(request, 'form.html', {'form': form})
    else:
        form = Form()
        return render(request, 'form.html', {'form': form})


