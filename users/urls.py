from .views import (CustomTokenObtainPairView,
					CustomTokenRefreshView,
					CustomTokenVerifyView,
					LogoutView,
					CustomProviderAuthView,
					UserView
					)
from django.urls import path, re_path


urlpatterns = [
	path('users/<int:pk>', UserView.as_view(), name="users_list"),
	path('jwt/create/', CustomTokenObtainPairView.as_view()),
	path('jwt/refresh/', CustomTokenRefreshView.as_view()),
	path('jwt/verify/', CustomTokenVerifyView.as_view()),
	path('logout/', LogoutView.as_view()),
	re_path(r'^o/(?P<provider>\S+)/$', CustomProviderAuthView.as_view(), name='provider_auth'),
]