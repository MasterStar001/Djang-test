from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Experience(request):
    return render(request, 'Experience.html')

def contact(request):
    if request.method =="POST":
        name = request.POSR.get('name')
        Phone = request.POST.get('Phone')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        contact = contact(name=name, Phone=Phone, massage=massage, email=email, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')