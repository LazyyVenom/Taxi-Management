from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import request
from .models import CustomUser,LiveLocation,Booking

def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,'login.html')

@csrf_exempt
def login_verify(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print(username,password)

        return render(request,'index.html')

    else:
        return 

def signup(request):
    return render(request,'signup.html')

@csrf_exempt
def register(request):
    if request.method == "POST":
        type_of_user = request.POST['type']
        name = request.POST['name']
        state = request.POST['state']
        pincode = request.POST['pincode']
        username = request.POST['username']
        password = request.POST['password']

        CustomUser.objects.create(
            username=username,
            password=password,
            pincode=pincode,
            name=name,
            state=state,
            type=type_of_user
            )
        
        print("DONE")

        return render(request,'signup.html')

    else:
        return 