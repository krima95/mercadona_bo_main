from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from mercadona import settings


urlpatterns = [
    path("admin/defender/", include('defender.urls')),  # defender admin
    path("admin/", admin.site.urls),  # admin
    path('', include('products.urls')),  # urls app products


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


