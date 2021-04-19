from django.contrib import admin
from django.urls import path, include

#fotoğrafların algılanması için işlemler
from django.conf.urls.static import static
from django.conf import settings

from blog.views import iletisim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #fotoğrafların algılanması için işlemler


