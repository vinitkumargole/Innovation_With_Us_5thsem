from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact,idea as Idea
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def detail(request):
    return render(request, 'details.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def signin(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password =request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect')

            context = {}
            return render(request, 'login.html')

def signup(request):
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    return redirect('login')
            context = {'form':form}
            return render(request, 'signup.html',context= context)


def learning(request):
    return render(request, 'learning.html')

def schemes(request):
    return render(request, 'schemes.html')

def idea(request):
   if request.method =="POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        profit = request.POST.get('profit')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        valuation = request.POST.get('valuation')
        companyname = request.POST.get('companyname')
        country = request.POST.get('country')
        file = request.POST.get('file')
        message = request.POST.get('message')
        idea= Idea(name=name, mobile=mobile,category=category,profit=profit,lastname=lastname,email=email,valuation=valuation,companyname=companyname,country=country,file=file, message=message, date=datetime.today())
        idea.save()
        messages.success(request, 'Your message has been send.')
   return render(request, 'ideaform.html')


def chatbot(request):
    return render(request, 'chatbot.html')

def contact1(request):
    return render(request, 'index/#section_5.html')


def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact= Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send.')
    return render(request,'index.html')
