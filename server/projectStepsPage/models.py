from ckeditor.fields import RichTextField
from django.db import models
from solo.models import SingletonModel


class ProjectStepsPage(SingletonModel):
    title = models.CharField(
        verbose_name="Заголовок страницы",
        max_length=255,
        default="Этапы выполнения работы"
    )

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Этапы выполнения работы"
        verbose_name_plural = "Этапы выполнения работы"


class ProjectSteps(models.Model):
    page = models.ForeignKey(
        ProjectStepsPage,
        verbose_name="Этапы выполнения работы",
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
        verbose_name = "Этап Выполнения"
        verbose_name_plural = "Этап Выполнения"
        ordering = ("order",)
