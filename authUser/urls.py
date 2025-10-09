from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from authUser import views


router = DefaultRouter()
router.register('profile', views.CustomUserViewSet, basename='CustomUser')


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'), 
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('current-user/', views.CurrentUserView.as_view(), name='current_user'),
    path('profile/', views.CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list_create'),
    path('profile/<int:pk>/', views.CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='profile_detail'),
    path('api/v1/', include(router.urls)),
]
