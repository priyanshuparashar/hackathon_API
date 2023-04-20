from rest_framework import serializers
from .models import *


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hackathon
        fields='__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


class ReistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reistration
        fields='__all__'
        

class ReistrationSerializer_2(serializers.ModelSerializer):
    
    hackathon_name = serializers.CharField(source='hackathon_id.title', read_only=True)

    class Meta:
        model = Reistration
        fields = ('id', 'user_id', 'hackathon_name', 'registration_date')
        
class DisplayUserHackathon(serializers.ModelSerializer):
    Hackathon_name = serializers.CharField(source='hackathon_id.title', read_only=True)
    Hackathon_Desc=serializers.CharField(source='hackathon_id.description', read_only=True)
    user_name = serializers.CharField(source='user_id.first_name', read_only=True)
    class Meta:
        
        model = Reistration
        fields = ('user_name', 'Hackathon_name', 'Hackathon_Desc')
    
    
class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Submission
        fields = '__all__'
