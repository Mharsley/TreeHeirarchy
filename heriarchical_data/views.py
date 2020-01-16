# from mptt.admin import DraggableMPTTAdmin
from heriarchical_data.models import File
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from heriarchical_data.forms import LoginForm
from django.contrib.auth.models import User


def register_user_view(request):
    html = 'file.html'
    page = 'register'

    if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                email=data['email']
            )
            login(request, u)
            return HttpResponseRedirect(reverse('homepage'))


@login_required
def home(request):
    html = 'index.html'
    data = File.objects.all()
    user = User.requestuser()
    return render(request, html, {'data': data, 'user': user})


def log(request):
    html = 'index.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def login_view(request):
    html = 'generic_form.html'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
        return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm()
    return render(request, html, {'form': form, 'page': page})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
