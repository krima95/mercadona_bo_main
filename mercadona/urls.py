from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from mercadona import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from django.conf import settings

from django.views.static import serve

urlpatterns = [
    path("admin/defender/", include('defender.urls')),  # defender admin
    path("admin/", admin.site.urls),  # admin
    path('', include('products.urls')),  # urls app products
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)