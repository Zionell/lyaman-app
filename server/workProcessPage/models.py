from ckeditor.fields import RichTextField
from django.db import models
from solo.models import SingletonModel


class WorkProcessPage(SingletonModel):
    title = models.CharField(
        verbose_name="Заголовок страницы",
        max_length=255,
        default="Процесс работы"
    )

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Процесс работы"
        verbose_name_plural = "Процесс работы"


class WorkProcess(models.Model):
    page = models.ForeignKey(
        WorkProcessPage,
        verbose_name="Процесс работы",
        on_delete=models.CASCADE,
        related_name="steps",
    )
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    text = RichTextField(verbose_name="Описание", blank=True)
    order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Процесс выполнения"
        verbose_name_plural = "Процесс выполнения"
        ordering = ("order",)
