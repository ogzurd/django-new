from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilDuzenlemeForm

@login_required(login_url='/')
def profil_duzenle(request):
    form = ProfilDuzenlemeForm(instance = request.user)
    if request.method == 'POST':
        form = ProfilDuzenlemeForm(request.POST, request.FILES, instance = request.user)
        #request.FILES yüklenen img vb dosyalar için gerekli.
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil başarıyla güncellendi.')
    else:
        form = ProfilDuzenlemeForm(instance = request.user)
    return render(request, 'pages/profil-guncelle.html', context={'form' : form})