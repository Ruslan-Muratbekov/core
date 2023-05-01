from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .api import RegisterGenericAPIView, LoginGenericAPIView, EventModelViewSet, EventUpdateModelViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('rest_framework.urls')),
    path('auth/register/', RegisterGenericAPIView.as_view()),
    path('auth/login/', LoginGenericAPIView.as_view()),

    path('event/', EventModelViewSet.as_view({'get': 'list'})),
    path('event/<int:pk>/', EventModelViewSet.as_view({'get': 'retrieve'})),
    path('event/update/<int:pk>/', EventUpdateModelViewSet.as_view()),
]
