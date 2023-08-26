from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import the view

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', obtain_auth_token, name='login'),  # Use obtain_auth_token here
    path('', include(router.urls)),
    # Add more URL patterns as needed
]
