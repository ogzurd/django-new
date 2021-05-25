from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login, authenticate


def kayit(request):
    form = KayitFormu()
    if request.method == 'POST':
        form = KayitFormu(request.POST)
        if form.is_valid():
            form.save() #kayıt olduk.
            username = form.cleaned_data.get('username') #username aldık
            password = form.cleaned_data.get('password1') #password aldık
            #bu kullanıcı adı ve şifreyi kullanarak direkt sisteme giriş yapmasını sağlamak.
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Aramıza Hoşgeldin! Başarıyla kayıt oluşturuldu.')
            return redirect('anasayfa')
        else:
            print('get')
        
        
    return render(request, 'pages/kayit.html', context={
        'form' : form
    })