from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return redirect('accounts:register')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required(login_url='accounts:login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('home:home')
