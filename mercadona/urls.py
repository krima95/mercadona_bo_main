from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from mercadona import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.views.static import serve

urlpatterns = [
    path("admin/defender/", include("defender.urls")),  # defender admin
    path("admin/", admin.site.urls),  # admin
    path("", include("products.urls")),  # urls app products
    path("django-check-seo/", include("django_check_seo.urls")),  # check SEO errors

    path("api/schema", SpectacularAPIView.as_view(), name="schema"),  # Swagger
    path(
        "api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")
    ),  # Swagger

    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs", SpectacularSwaggerView.as_view(url_name="schema")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
