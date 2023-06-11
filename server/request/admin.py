from django.contrib import admin

from .models import Request


class RequestAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Request, RequestAdmin)
