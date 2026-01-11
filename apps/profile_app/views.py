from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.skills.models import Skill
from apps.projects.models import Project
from .models import Profile
from .serializers import ProfileSerializer

class ProfileAPIView(APIView):
    def get(self, request):
        profile = Profile.objects.first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def home_view(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'index.html', context)