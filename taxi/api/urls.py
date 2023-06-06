from rest_framework.routers import DefaultRouter

from taxi.api.views import RideViewSet

router = DefaultRouter()
router.register('ride', RideViewSet, basename='ride')
urlpatterns = router.urls
