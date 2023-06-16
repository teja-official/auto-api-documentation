from rest_framework.routers import DefaultRouter
from myapp.views import PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
urlpatterns = router.urls