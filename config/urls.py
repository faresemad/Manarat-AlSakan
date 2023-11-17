from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="not-found.html"), name="not-found"),
    path(f"{settings.ADMIN_URL}", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    path(f"{settings.API_PREFIX}auth/", include("djoser.urls.jwt")),
]

urlpatterns += [
    path(f"{settings.API_PREFIX}accounts/", include("apps.accounts.api.urls")),
]
