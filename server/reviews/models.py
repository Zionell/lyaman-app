from ckeditor.fields import RichTextField
from django.db import models
from solo.models import SingletonModel


class ReviewsPage(SingletonModel):
    title = models.CharField(
        verbose_name="Заголовок страницы",
        max_length=255,
        default="Отзывы"
    )

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"


class Reviews(models.Model):
    page = models.ForeignKey(
        ReviewsPage,
        verbose_name="Отзывы",
        on_delete=models.CASCADE,
        related_name="review",
    )
    title = models.CharField(verbose_name="Автор", max_length=255)
    text = RichTextField(verbose_name="Отзыв", blank=True)
    order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отзывы"
        verbose_name_plural = "Отзывы"
        ordering = ("order",)
