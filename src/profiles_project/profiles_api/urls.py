from django.urls import path
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # Add more URL patterns as needed
]

