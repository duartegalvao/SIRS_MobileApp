import json
import requests
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import RemoteAuthenticationForm
from .models import TwoFactor
from .decorators import login_required_SIRS
import pyotp
import time
import datetime


@login_required_SIRS
def home(request):
    totp = pyotp.TOTP(TwoFactor.objects.first().totp_key)
    code = totp.now()
    refresh_in = code_refresh(datetime.datetime.now(), totp.interval)

    return render(request, 'mobile_app/home.html', {'refresh': refresh_in, 'code': code, 'loggedIn': True})


def code_refresh(for_time, interval=30):
    return interval - (time.mktime(for_time.timetuple()) % interval)


def login_view(request):
    if request.method == 'POST':
        form = RemoteAuthenticationForm(data=request.POST)
        print("validating")
        if form.is_valid():
            print("validated")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            payload = {
                "username": username,
                "password": password
            }

            r = requests.post("https://sirs.galvao.xyz/api/login/?format=json", data=payload)

            resp = json.loads(r.text)

            if r.status_code == 200:
                if resp['secret'] is None:
                    messages.error(request, 'Unknown error.')
                else:
                    two_fact = TwoFactor(totp_key=resp['secret'])
                    two_fact.is_logged_in = True
                    two_fact.username = username
                    two_fact.save()

                    messages.success(request, f'{username} is logged in!\n Two step authentication is now enabled')
                    return redirect('index')
            elif r.status_code == 400:
                if resp['error'] is not None and resp['error'] == "notFirstLogin":
                    messages.error(request, 'Credentials error.')
                elif resp['error'] is not None and resp['error'] == "badRequest":
                    messages.error(request, 'Unknown error.')
                else:
                    messages.error(request, 'Unknown error.')
            elif r.status_code == 401:
                if resp['error'] is not None and resp['error'] == "notFirstLogin":
                    messages.error(request, 'Not first login. Please contact web app administrators.')
                else:
                    messages.error(request, 'Unknown error.')
            elif r.status_code == 500:
                messages.error(request, 'Unknown error.')
            else:
                messages.error(request, 'Unknown error.')

        return render(request, 'mobile_app/login.html', {'form': form})
    else:
        form = RemoteAuthenticationForm()
        return render(request, 'mobile_app/login.html', {'form': form})


@login_required_SIRS
def logout_view(request):
    two_factor = TwoFactor.objects.first()
    username = two_factor.username
    totp_key = two_factor.totp_key

    payload = {
        "username": username,
        "totp_key": totp_key
    }

    r = requests.post("https://sirs.galvao.xyz/api/logout/?format=json", data=payload)

    if r.status_code == 200:
        two_factor.delete()
        return redirect('index')
    else:
        messages.error(request, 'Unknown error.')
        return render(request, 'mobile_app/home.html', {'refresh': False, 'code': "", 'loggedIn': False})
