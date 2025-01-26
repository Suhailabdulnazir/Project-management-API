from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet,RegisterUserView, LoginUserView
from rest_framework.authtoken import views as authtoken_views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', LoginUserView.as_view(), name='login'),
    path('api/token-auth/', authtoken_views.obtain_auth_token, name='token-auth'),

]
