from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import WorkProcessPage, WorkProcess


class _WorkProcessInline(admin.StackedInline):
    model = WorkProcess
    extra = 0
    classes = ("collapse",)


@admin.register(WorkProcessPage)
class WorkProcessPageAdmin(SingletonModelAdmin):
    inlines = [
        _WorkProcessInline,
    ]
