from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import CertificatesPage, Certificates


class _CertificatesInline(admin.StackedInline):
    model = Certificates
    extra = 0
    classes = ("collapse",)


@admin.register(CertificatesPage)
class CertificatesPageAdmin(SingletonModelAdmin):
    inlines = [
        _CertificatesInline,
    ]
