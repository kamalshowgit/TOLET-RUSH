from email import message
from showstatic.models import saveforms
from django.contrib import messages
from django.shortcuts import render

def home(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "Home.html")

def contact(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "contact.html")

def index(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")

def photos(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "photos.html")

def mywork(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "mywork.html")

def saveform(request):
    if request.method == 'POST':
        contactName = request.POST.get('contactName')
        contactEmail = request.POST.get('contactEmail')
        contactSubject = request.POST.get('contactSubject')
        contactMessage = request.POST.get('contactMessage')
        
        data = saveforms(
        contactName=contactName, 
        contactEmail=contactEmail, 
        contactSubject=contactSubject, 
        contactMessage=contactMessage)
        data.save()
        # messages.success('message-success')
        return render(request,"index.html")