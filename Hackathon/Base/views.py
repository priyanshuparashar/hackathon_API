from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.decorators import *
from django.contrib.auth.decorators import *

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAdminUser

# Create your views here.


# api post request to create a hackathon
# only admin can create a hackathon
#you can create a new superuser to login or use the default one passeord: admim username admin

@api_view(['POST'])
@permission_classes([IsAdminUser])
def HackathonPost(request):
    serializer = HackathonSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# api request to list all the hackathon

@api_view(['GET'])
def Hackathonget(request):
    hackathons=Hackathon.objects.all()
    
    serializer = HackathonSerializer(hackathons,many=True)
    
    return Response(serializer.data)

#api to get all the registartion
@api_view(['GET'])
def Registrationget(request):
    reistration = Reistration.objects.all()

    serializer = ReistrationSerializer_2(reistration, many=True)

    return Response(serializer.data)

# api to post request to register for a hackathon
@api_view(['POST'])
def RegistrationPost(request):
    serializer = ReistrationSerializer(data=request.data)
    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetUserHackathon(request, username=None):
    
    u_id = User.objects.get(Username=username)
    user_registration = Reistration.objects.filter(user_id=u_id)
   
    serializer = DisplayUserHackathon(user_registration, many=True)

    return Response(serializer.data)


# to create a post request to user
@api_view(['POST'])
def create_submission(request, username, hackathon):
    user_id = User.objects.get(Username=username)
    hackathon_id = Hackathon.objects.get(id=hackathon)
    try:
        # Check if the user is registered for the hackathon
        registration = Reistration.objects.get(
            user_id=user_id, hackathon_id=hackathon_id)
        

        # Create a new submission for the user and hackathon
        submission = Submission(
            user_id=user_id,
            hackathon_id=hackathon_id,
            submission_name=request.data['submission_name'],
            summary=request.data['summary']
        )
        submission.save()

        # Return a success response
        return Response({'message': 'Submission created'}, status=status.HTTP_201_CREATED)

    except Reistration.DoesNotExist:
        # If the user is not registered for the hackathon, return an error response
        return Response({'error': 'User is not registered for the hackathon'}, status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        # If the submission data is invalid, return an error response
        return Response({'error': 'Invalid submission data'}, status=status.HTTP_400_BAD_REQUEST)

# to list all the submission made my user
@api_view(['GET'])
def Submissionget(request, username):
    u_id = User.objects.get(Username=username)
    submission = Submission.objects.filter(user_id=u_id)

    serializer = SubmissionSerializer(submission, many=True)

    return Response(serializer.data)
