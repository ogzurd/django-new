from django.contrib import admin
from django.urls import path, include

#fotoğrafların algılanması için işlemler
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #fotoğrafların algılanması için işlemler


