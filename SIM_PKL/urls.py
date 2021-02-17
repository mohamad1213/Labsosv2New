from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    # path('staf/', include('staf.urls')),
    path('catatan/', include('catatan.urls')),
    path('catatan.d/',include('catatan.urls_dosen')),
    path('accounts/', include('accounts.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('mahasiswas/', include('mahasiswa.urls_staf')),
    path('dosenah/', include('mahasiswa.urls_dosen')),
    path('dosens/', include('dosen.urls_staf')),
    path('forums/', include('forum.urls_staf')),
    path('forumd/', include('forum.urls_dosen')),
    path('forum/', include('forum.urls')),
    path('verification/', include('accounts.urls')),	
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


