from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q #ya da işlemi için kullanılır

def anasayfa(request):

    yazilar = YazilarModel.objects.order_by("-olusturulma_tarihi")
    sayfa = request.GET.get('sayfa')
    #localhost:8000/?sayfa=2 diyebilmek için alacağız.

    sorgu = request.GET.get('sorgu') #search işlemleri için bir /?sorgu= oluşturduk
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)

        ).distinct()


    paginator = Paginator(yazilar, 3) #anasayfadaki kayıt sayısı.. (bir sayfada kaç kayıt olsun?)
    return render(request, "pages/anasayfa.html", context={
        "yazilar":paginator.get_page(sayfa)  #/?sayfa=1 gibi isteklerimizi belirttik.
        })
    
    # yazilar.has_previous, sayfamızın bir önceki sayfası var mı anlamına gelen komut.
    # yazilar.previous_page_number, anlık sayfamızın bir önceki sayfa numarasına tekabül eder. href verirken kullanılır.
    # yazilar.has_next, sayfamızın bir sonraki sayfası var mı kontrolü için kullanılır.
    # yazilar.next_page_number, sayfamızın bir sonraki numarasını temsil eder.