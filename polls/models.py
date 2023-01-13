from django.db import models
from django.urls import reverse

class Mein(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Date(models.Model):
    name = models.CharField(max_length=255)
    salary = models.FloatField(verbose_name="Оклад")
    salary_currency = models.TextField(blank=True, verbose_name="Валюта")
    area_name = models.TextField(blank=True)
    published_at = models.DateField(verbose_name="Время публикации")
    cat = models.ForeignKey("decemberDay", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class decemberDay(models.Model):
    decDay = models.DateField(verbose_name="Дата публикации", db_index=True)

