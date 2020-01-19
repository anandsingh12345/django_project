from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from employee.models import Employee 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    count = User.objects.count()
    employeecount = Employee.objects.count()
    return render(request,'home.html',{'count':count,'ecount':employeecount})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})    
