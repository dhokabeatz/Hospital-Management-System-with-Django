from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request,'contact.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request,'login.html')


def Logout(request):
    logout(request)
    return redirect('login')

