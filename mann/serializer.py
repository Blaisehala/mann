from rest_framework import serializers
from .models import Profile, Project



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('user', 'image')




class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =('title', 'description', 'image', 'link', 'user')