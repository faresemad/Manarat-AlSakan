from rest_framework.routers import DefaultRouter

from apps.estates.api.views import EstatsViewSet

router = DefaultRouter()

router.register(r"estates", EstatsViewSet, basename="estates")

urlpatterns = router.urls
