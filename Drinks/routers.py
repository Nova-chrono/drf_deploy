from rest_framework.routers import DefaultRouter
from .views import DrinkViewSet


router = DefaultRouter()
router.register('drinks', DrinkViewSet)


urlpatterns = router.urls