from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .api import RegisterGenericAPIView, LoginGenericAPIView, EventModelViewSet, EventUpdateModelViewSet, \
    EventDestroyAPIView, ThemeReadonlyAPIView, EventCreateModelAPIView, EventSubscribeModelViewSet, \
    EventSubscribeReadonlyAPIView, EventDeleteSubscribeAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # прошел тест
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # прошел тест
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # прошел тест

    path('auth/', include('rest_framework.urls')),  # прошел тест
    path('auth/register/', RegisterGenericAPIView.as_view()),  # прошел тест
    path('auth/login/', LoginGenericAPIView.as_view()),  # прошел тест

    path('event/', EventModelViewSet.as_view({'get': 'list'})),  # прошел тест
    path('event/<int:pk>/', EventModelViewSet.as_view({'get': 'retrieve'})),  # прошел тест
    path('event/create/', EventCreateModelAPIView.as_view()),  # прошел тест
    path('event/update/<int:pk>/', EventUpdateModelViewSet.as_view()),  # прошел тест
    path('event/delete/<int:pk>/', EventDestroyAPIView.as_view()),  # прошел тест

    path('event/subscribe/', EventSubscribeReadonlyAPIView.as_view({'get': 'list'})),  # прошел тест
    # path('event/subscribe/<int:pk>/', EventSubscribeReadonlyAPIView.as_view()),  # прошел тест (сокращение кода)
    path('event/add/subscribe/<int:pk>/', EventSubscribeModelViewSet.as_view()),  # прошел тест
    path('event/delete/subscribe/<int:pk>/', EventDeleteSubscribeAPIView.as_view()),  # прошел тест

    path('theme/', ThemeReadonlyAPIView.as_view({'get': 'list'})), # прошел тест
    path('theme/<int:pk>/', ThemeReadonlyAPIView.as_view({'get': 'retrieve'})), # прошел тест
]

# 2.3.1. Пользователь должен иметь возможность искать события по различным параметрам, например, по теме, местоположению, формату и дате проведения. - все!!!!!!

# 2.4.3. Пользователь должен иметь возможность связываться с организаторами событий.

# 2.5. Рейтинг событий

# 2.5.1. Пользователь должен иметь возможность оставлять отзывы о событиях и ставить им оценки.

# 2.5.2. Пользователь должен иметь возможность просматривать рейтинг событий.
