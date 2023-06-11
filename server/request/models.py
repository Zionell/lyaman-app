from ckeditor.fields import RichTextField
from django.db import models


class Request(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    email = models.CharField(verbose_name="Почта", max_length=255)
    comment = RichTextField(verbose_name="Комментарий", blank=True)

