from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import ProjectStepsPage, ProjectSteps


class _ProjectStepsInline(admin.StackedInline):
    model = ProjectSteps
    extra = 0
    classes = ("collapse",)


@admin.register(ProjectStepsPage)
class ProjectStepsPageAdmin(SingletonModelAdmin):
    inlines = [
        _ProjectStepsInline,
    ]
