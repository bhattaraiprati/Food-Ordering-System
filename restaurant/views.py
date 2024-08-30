from django.shortcuts import render, redirect

# Create your views here.

def register_page(request):

    # return redirect("register.html")
    
    return render(request, "register.html")

def signin_page(request):

    # return redirect("login.html")
    return render(request, "login.html")

def signup_page(request):
    # return redirect("signup.html")
    return render(request,"signup.html")


