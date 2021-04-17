from django.contrib import admin
from blog.models import KategoriModel, YazilarModel
# Register your models here.



class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik') #baslik ve içeriğe göre arama butonu ekleidk
    list_display = (
        'baslik' , 'olusturulma_tarihi', 'duzenlenme_tarihi'
    ) #admin sayfasında görüntülenen verilerin yanına tarihlerini de ekledik.



admin.site.register(KategoriModel)
admin.site.register(YazilarModel, YazilarAdmin)