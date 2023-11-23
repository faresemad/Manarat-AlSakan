from rest_framework.routers import DefaultRouter

from apps.estates.api.views import EstateRatingViewSet, EstatsViewSet

router = DefaultRouter()

router.register(r"estates", EstatsViewSet, basename="estates")
router.register(r"estates/(?P<estate_slug>[-\w]+)/ratings", EstateRatingViewSet, basename="estate_ratings")

urlpatterns = router.urls
