from django.shortcuts import render, redirect


def home(request):
    return render(request, 'mobile_app/home.html')


def login_view(request):
    return redirect('index')
