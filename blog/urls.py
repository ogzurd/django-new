from django.urls import path

from blog.views import iletisim, anasayfa, kategori, yazilarim, detay, yazi_ekle, yazi_guncelle, yazi_sil, yorum_sil, email_gonderildi

from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', anasayfa, name = "anasayfa"),
    path('iletisim', iletisim, name = "iletisim"),
    #linklere href verirken {%url 'name'%} olarak gönderebiliriz.
    path('kategori/<slug:kategoriSlug>', kategori, name="kategori"),
    #slug türünde, kategoriSlug adında bir path verdik.
    #yani /doga-olaylari/tsunami şeklinde bir linkimiz olacak.
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
    path('yazi-ekle', yazi_ekle, name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>', yazi_guncelle, name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>', yazi_sil, name="yazi-sil"),
    path('yorum-sil/<int:id>', yorum_sil, name="yorum-sil"),
    path('hakkimda', TemplateView.as_view(
        template_name = "pages/hakkimda.html"
    ), name="hakkimda"), #templateview ile direkt templatelere erişebiliriz.
    path('yonlendir', RedirectView.as_view(
        url = "https://www.google.com"
    ), name="yonlendir"), #direkt yonlendirme için redirectview kullanılabilir.
    path('email-gonderildi', email_gonderildi, name='email-gonderildi'),
]   
