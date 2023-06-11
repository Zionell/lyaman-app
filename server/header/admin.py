from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Header

admin.site.register(Header, SingletonModelAdmin)
