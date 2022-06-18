from django.shortcuts import render
from .models import Event
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def shop(request):
    return render(request,'shop.html')
def bookticket(request):
    return render(request,'book_ticket.html') 
def event(request):
    objs=Event.objects.all()

    return render(request,'event.html',{'dests':objs})   
    