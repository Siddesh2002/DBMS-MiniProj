from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def shop(request):
    return render(request,'shop.html')
def register(request):
    return render(request,'register.html')
def bookticket(request):
    return render(request,'book_ticket.html')    
    