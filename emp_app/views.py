from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello, welcome to the Employee Portal!</h1>")
def emp(request):
    return render(request,'employee.html')
