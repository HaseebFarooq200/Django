from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Users
from .serializer import DataSerializer
from .serializer import LoginSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import Users
# Create your views here.

# Create a USER Register


@api_view(['POST'])
def create_record(request):
    if (request.method == 'POST'):
        serializedData = DataSerializer(data=request.data)
        if serializedData.is_valid():
            # Save the instance to the database
            serializedData.save()
            print('Record created successfully', serializedData.data)
            return Response(serializedData.data)
        else:
            print('Error Occurred')
            return Response({'message': 'Error Occurred'})


# Login a User
@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Authenticate the user by email and password
        user = authenticate(email=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            print("Sign-in successful", user)
            return Response({"message": "Sign-in successful"})
        else:
            print("Invalid credentials")
            return Response({"message": "Invalid credentials"})
    else:
        # Print the serializer errors for debugging
        print("Serializer errors:", serializer.errors)

    # If serializer is not valid, return validation errors
    return Response(serializer.errors, status=400)

# Get All users
@api_view(['GET'])
def GetUsers(request):
    users = Users.objects.all()
    serializer = DataSerializer(users, many=True)
    print(serializer.data)
    return Response(serializer.data)

# Get UserbyID


@api_view(['GET'])
def GetUserbyId(request, userId):
    users = Users.objects.get(id=userId)
    serializer = DataSerializer(users, many=False)
    print(serializer.data)
    return Response(serializer.data)
