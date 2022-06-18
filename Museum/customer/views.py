from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import Event
from django.contrib import messages
price=0
nme=""
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
def printreceipt(request):
    return render(request,'printreceipt.html')    
def ticket_view(request,det_id):
    try:
        eid=Event.objects.get(id=det_id)
    except Event.DoesNotExist:
        messages.info('Event: Id not found')
    price=int(eid.price)
    nme=eid.name
    return render(request,'book_ticket.html',{'ename':eid.name})
def calculate(request):
    user_detail=request.user
    no=int(request.POST['nopersons'])
    dob=request.POST['dob']
    amount=price*no
    print(amount)
    print(nme)
    return render(request,'printreceipt.html',{'amount':amount,'Firstname':user_detail.first_name, 'Lastname':user_detail.last_name,'nopersons':no,'dob':dob,'eid':nme})
    

