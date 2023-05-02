from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .api import *

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

	path('theme/', ThemeReadonlyAPIView.as_view({'get': 'list'})),  # прошел тест
	path('theme/<int:pk>/', ThemeReadonlyAPIView.as_view({'get': 'retrieve'})),  # прошел тест

	path('comments/add/', EventCommentsAddAPIView.as_view()),
	path('comments/remove/', EventCommentsDeleteAPIView.as_view()),

	path('rating/', EventRatingAPIView.as_view())
]

# 2.4.3. Пользователь должен иметь возможность связываться с организаторами событий.