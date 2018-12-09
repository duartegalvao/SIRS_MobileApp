from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RemoteAuthenticationForm(AuthenticationForm):
    #override
    def clean(self):
        return self.cleaned_data

    #override
    def confirm_login_allowed(self, user):
        pass
