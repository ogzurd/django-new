from django.db import models
from autoslug import AutoSlugField


class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from = "isim", unique = True)
    #isimden türettiğimiz bir eşşiz bir slug türettik. blog.com/doga-olaylari/

    class Meta:

        db_table = "kategori" #sqlite de görünen tablo ismi
        verbose_name_plural = "Kategoriler" #admin panelinde tablo adımız Kategoriler olarak değişti
        verbose_name =  "Kategori" #select Kategori olarak değiştirdik.
 
    def __str__(self):
        return self.isim #tablodaki verilerin ismi ile gözükmesini sağladık