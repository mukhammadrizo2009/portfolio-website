from django.urls import path
from .views import SkillAPIView

urlpatterns = [
    path('skills/', SkillAPIView.as_view()),
]