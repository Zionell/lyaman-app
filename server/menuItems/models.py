from django.db import models


class MenuItems(models.Model):
    label = models.CharField(verbose_name="Название пункта", max_length=255)
    value = models.CharField(verbose_name="Алиас", max_length=255)

