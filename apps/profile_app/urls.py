from django.urls import path
from .views import ProfileAPIView, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('profile/', ProfileAPIView.as_view()),
]