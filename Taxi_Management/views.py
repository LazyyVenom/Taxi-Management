from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,'login.html')

@csrf_exempt
def login_verify(request):
    print("Login Verify")
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

@csrf_exempt
def register(request):
    print("Register")
    return render(request,'signup.html')