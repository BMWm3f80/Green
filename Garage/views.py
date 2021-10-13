from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from balance import main_service


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'form', form})

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form', form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['apps'] = main_service.get_user_privilages(user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect("Your account has been disabled")
        else:
            return render(request, 'login.html', {"error": "Incorrect username or password"})
    else:
        return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('/')

