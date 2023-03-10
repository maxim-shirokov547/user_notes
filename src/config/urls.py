from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.internal.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = 'api.pkg.errors.handler500'
handler400 = 'api.pkg.errors.handler400'
handler404 = 'api.pkg.errors.handler404'
handler403 = 'api.pkg.errors.handler403'
