from django.db import models


class Contacts(models.Model):
    name = models.CharField(verbose_name="Название соцсети", max_length=255)
    link = models.CharField(verbose_name="Ссылка", max_length=255)

