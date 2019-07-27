from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    storage = messages.get_messages(request)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You account has being created\
                successfully. You can login now.")
            return redirect('accounts:login')
        else:
            messages.error(request, "Your passwords do not match or \
                they are weak. Type a stronger(longer) password.\
                Must be letters and numbers.")
            return redirect('accounts:register')
    else:
        form = UserCreationForm()
        args = {'form':form,'messages': storage}
    return render(request, 'accounts/register.html', args)


def login_view(request):
    storage = messages.get_messages(request)
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home:home')
    else:
        form = AuthenticationForm()
        args = {'form':form, 'messages': storage}
    return render(request, 'accounts/login.html', args)

@login_required(login_url='accounts:login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect('home:home')
