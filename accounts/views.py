from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method=='POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    if request.user.is_authenticated:
        msg = f"user is authenticated as {request.user.username}"
    else:
        msg = "user is not authenticated"
    return render(request, 'accounts/login.html',{'msg':msg})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    return render(request, 'accounts/signup.html')