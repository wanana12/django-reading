from django.db import models


class Reading(models.Model):
    title = models.CharField("タイトル", max_length=30)
    writer = models.CharField("著者", max_length=30)
    detail = models.TextField("詳細", blank=True)
    date = models.DateField("読了日")

    def __str__(self):
        return self.title