from django.shortcuts import render

def index(request):
    print("Here")
    return render(request,"index.html")