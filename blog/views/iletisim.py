from django.shortcuts import render,redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm()
    #formda submit ettiğimiz veriler post olarak yollanacak.
    if request.method == "POST":
        #request.POST post edilen bütün verileri queryset olarak döndürür.
        form = IletisimForm(request.POST)
        if form.is_valid():
            #form.cleaned_data['mesaj'] veya form.cleaned_data.get('mesaj') ile formdan gelen verileri alabiliriz.
            iletisim = IletisimModel()
            iletisim.email = form.cleaned_data['email']
            iletisim.isim_soyisim = form.cleaned_data['isim_soyisim']
            iletisim.mesaj = form.cleaned_data['mesaj']
            iletisim.save()

            #forms.ModelForm clasını kullandığımız için yukarıdakilerin hiçbiriniz yazmayıp
            #sadece form.save() deseydik de yeterli olacaktır.
            return redirect('anasayfa')
        else:
            print("valid değil")
    return render(request,"pages/iletisim.html", context = {'form':form})
    