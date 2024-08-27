from django.shortcuts import render

# Create your views here.

def register_page(request):

    
    return render(request, "register.html")

def signup_page(request):

    
    return render(request, "login.html")


