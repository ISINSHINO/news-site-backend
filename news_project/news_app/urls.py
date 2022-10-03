from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news_app.views import PostViewSet
from news_app.views import TagViewSet
from news_app.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
   path('', include(router.urls)),
   path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)