from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . views import RegisterAPIView,LogOutAPIView

urlpatterns=[
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/',RegisterAPIView.as_view(),name="register_api"),
    path('api/logout/',LogOutAPIView.as_view(),name="logout_api")
    
]