from rest_framework.routers import DefaultRouter

from payment.api.views import PaymentViewSet, PaymentMethodViewSet, DiscountViewSet

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'payment_method', PaymentMethodViewSet, basename='payment_method')
router.register(r'discount', DiscountViewSet, basename='discount')

urlpatterns = router.urls
