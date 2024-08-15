from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
   #messages.success(request,'hy i am here')
   return render(request, 'index.html')
   # return HttpResponse("this is home page") 

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,mobileno=mobileno,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message is send')
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")
       
    