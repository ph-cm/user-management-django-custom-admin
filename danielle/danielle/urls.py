from django.contrib import admin
from django.urls import path, include

from people.views import UserCreate, CustomObtainAuthToken, UserRetrieve, dashboard_view
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard', dashboard_view, name='dashboard'),

    # API
    path('api/v1/', include('people.urls')),

    # auth
    path('users/', UserCreate.as_view(), name='user_create'),
    path('users/<int:pk>/', UserRetrieve.as_view(), name='user_retrieve'),
    path("login/", CustomObtainAuthToken.as_view(), name="login"),
    path('api-token-auth/', obtain_auth_token, name='api_token_path'),

    # schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # swagger
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]