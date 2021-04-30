from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None) # if request.method == post yapmak yerine..

    if form.is_valid():
        yazi = form.save(commit=False) #bütün veriyi hazırla ama kaydetme
        yazi.yazar = request.user  #yazarı kullanıcı olarak belirle
        yazi.save()  #ve kaydet
        form.save_m2m() #kategorideki verileri kaydetmek için manytomany kaydı yaptık.  
        return redirect('detay', slug = yazi.slug)



    return render(request, 'pages/yazi-ekle.html', context={
        'form' : YaziEkleModelForm
    })