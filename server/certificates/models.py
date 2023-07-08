from django.db import models
from solo.models import SingletonModel


class CertificatesPage(SingletonModel):
    title = models.CharField(
        verbose_name="Заголовок страницы",
        max_length=255,
        default="Сертификаты"
    )

    def __str__(self):
        return self._meta.verbose_name

    class Meta:
        verbose_name = "Сертификаты"
        verbose_name_plural = "Сертификаты"


class Certificates(models.Model):
    page = models.ForeignKey(
        CertificatesPage,
        verbose_name="Сертификаты",
        on_delete=models.CASCADE,
        related_name="certs",
    )
    text = models.CharField(verbose_name="название сертификата", max_length=255)
    image = models.ImageField(
        verbose_name="Изображение", upload_to="static/images/certificates", blank=True, null=True
    )
    order = models.PositiveSmallIntegerField(
        verbose_name="Порядок",
        default=0,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Сертификаты"
        verbose_name_plural = "Сертификаты"
        ordering = ("order",)
