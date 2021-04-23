from django.urls import path

from blog.views import iletisim, anasayfa, kategori, yazilarim

urlpatterns = [
    path('', anasayfa, name = "anasayfa"),
    path('iletisim', iletisim, name = "iletisim"),
    #linklere href verirken {%url 'name'%} olarak gönderebiliriz.
    path('kategori/<slug:kategoriSlug>', kategori, name="kategori"),
    #slug türünde, kategoriSlug adında bir path verdik.
    #yani /doga-olaylari/tsunami şeklinde bir linkimiz olacak.
    path('yazilarim', yazilarim, name='yazilarim')
]
