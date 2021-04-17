from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel
# Register your models here.


@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik','icerik') #baslik ve içeriğe göre arama butonu ekleidk
    list_display = (
        'baslik' , 'olusturulma_tarihi', 'duzenlenme_tarihi'
    ) #admin sayfasında görüntülenen verilerin yanına tarihlerini de ekledik.


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = (
        'yazan', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )
    search_fields = ('yazan__username',)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = (
        'isim_soyisim', 'email', 'mesaj', 'olusturulma_tarihi'
    )
    search_fields = ('mesaj','email')


admin.site.register(KategoriModel)


