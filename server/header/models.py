from ckeditor.fields import RichTextField

from django.db import models
from solo.models import SingletonModel


class Header(SingletonModel):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = RichTextField(verbose_name="Описание", blank=True)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="static/images/", blank=True, null=True
    )
    tag1 = models.CharField(verbose_name="Тег 1", max_length=100)
    tag2 = models.CharField(verbose_name="Тег 2", max_length=100)
    btnText = models.CharField(verbose_name="Текст в кнопке", max_length=100)

    class Meta:
        verbose_name = "Главный экран"
        verbose_name_plural = "Главный экран"

    def __str__(self):
        return f"{self.title}"