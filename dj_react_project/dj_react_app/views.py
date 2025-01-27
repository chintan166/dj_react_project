from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import RegisterSerializer, LoginSerializer

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Access validated data after serializer is valid
            username = serializer.validated_data['user'].username  # Get the username of the authenticated user
            # or use email if you want
            password = serializer.validated_data['password']  # Access the password for the user
            
            # Authenticate user using validated data
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({"message": "Login successful"})
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
