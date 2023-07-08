from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import ReviewsPage, Reviews


class _ReviewsInline(admin.StackedInline):
    model = Reviews
    extra = 0
    classes = ("collapse",)


@admin.register(ReviewsPage)
class ReviewsPageAdmin(SingletonModelAdmin):
    inlines = [
        _ReviewsInline,
    ]
