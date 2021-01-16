from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import SignUpAPIView

urlpatterns = [
    path(
        'signup/',
        SignUpAPIView.as_view(),
    ),
    path(
        'token/',
        jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'),
]
