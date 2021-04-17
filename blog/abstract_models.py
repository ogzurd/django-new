from django.db import models


class DateTimeAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #otomatik olarak o tarih oluşturulacak
    duzenlenme_tarihi = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True