from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from hospital.forms import CustomRegistrationForm

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


def Register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to login page for user to login after registerting
        else:
            form = CustomRegistrationForm()
        return render(request,'register.html',{'form':form})


