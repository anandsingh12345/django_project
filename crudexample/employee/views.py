from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
from .filters import EmployeeFilter
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
@login_required    
def show(request):  
    employees = Employee.objects.order_by('-dateofjoining','name')
    totalcount = employees.count()
    myfilter = EmployeeFilter(request.GET,queryset=employees)
    employees = myfilter.qs
    return render(request,"show.html",{'employees':employees,'myfilter':myfilter,'totalcount':totalcount})


@login_required 
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

@login_required 
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

@login_required     
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer