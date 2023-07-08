from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django .http import HttpResponse
from . models import Nikeshoe
# Create your views here.
def index(request):
    nikeshoe=Nikeshoe.objects.all()
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        # authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have logged in')
            return redirect('/')
        else:
            messages.success(request,'Please check your credentials')
            return redirect('/')
    else:

         return render(request, 'index.html')


def logout_user(request):
    logout(request)
    messages.success(request, ' successfully logouted')
    return redirect('index')


def detail(request,id):
    nikeshoe=Nikeshoe.objects.get(id=id)
    return render(request,"detail.html" ,{'nikeshoe':nikeshoe})

def card(request):
    nikeshoe=Nikeshoe.objects.all()
    return render(request,'card.html',{'nikeshoe':nikeshoe})


def home(request):
    return render(request,'home.html')