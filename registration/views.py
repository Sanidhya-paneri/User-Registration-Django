from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

#User-management
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#forms
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'registration/index.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/registration')

    params = {}
    return render(request, 'registration/login.html', params)

def logoutPage(request):
    logout(request)
    return  redirect('login')




def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    params = {'form': form}
    return render(request, 'registration/register.html', params)

