from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='food')
urlpatterns = router.urls
