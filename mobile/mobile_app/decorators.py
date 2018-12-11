from django.shortcuts import redirect
from .models import TwoFactor


def login_required_SIRS(function):
    def wrap(request, *args, **kwargs):
        twoFactor = TwoFactor.objects.first()

        if twoFactor is not None:
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap
