from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={'variable':"this is sernt"}
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Your response has been recorded.')

    return render(request,'contact.html')

