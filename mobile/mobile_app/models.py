from django.db import models
from django.contrib import admin


class TwoFactor(models.Model):
    totp_key = models.CharField(max_length=70, default="", null=False)

class MyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = TwoFactor.objects.all().count()
        if count == 0:
            return True

        return False
