from ckeditor.fields import RichTextField
from django.db import models

from django.db import models


class HeaderAbstract(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text = RichTextField(verbose_name="Описание", blank=True)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="static/images/", blank=True, null=True
    )
    tag1 = models.CharField(verbose_name="Тег 1", max_length=100)
    tag2 = models.CharField(verbose_name="Тег 2", max_length=100)
    btnText = models.CharField(verbose_name="Текст в кнопке", max_length=100)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance


class Header(HeaderAbstract):
    tag1 = models.CharField(verbose_name="Тег 1", max_length=100)
    tag2 = models.CharField(verbose_name="Тег 2", max_length=100)
    btnText = models.CharField(verbose_name="Текст в кнопке", max_length=100)
