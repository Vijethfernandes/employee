from django.shortcuts import render,redirect
from emp_app.forms import Add_emp

from django.http import HttpResponse

def add_emp(request):
    name=Add_emp(request.POST)
    if name.is_valid():
        name.save()

    
    return render(request,'add_emp.html',{'data':name})
