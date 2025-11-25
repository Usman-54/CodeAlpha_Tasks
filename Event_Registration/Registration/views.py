from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import CustomUser, Event, registration
from django.contrib.auth import authenticate
from .serializers import UserSignupSerializer, UserLoginSerializer, EventSerializer, RegistrationSerializer

# Signup
class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]  # <--- anyone can POST

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    # Login
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]  # anyone can access

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'User logged in successfully'},
                            status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterEventView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if registration.objects.filter(user=request.user, event=event, cancelled=False).exists():
            return Response({'detail': 'Already registered'}, status=status.HTTP_400_BAD_REQUEST)
        reg = registration.objects.create(user=request.user, event=event)
        return Response(RegistrationSerializer(reg).data, status=status.HTTP_201_CREATED)

class UserRegistrationListView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return registration.objects.filter(user=self.request.user)

class CancelRegistrationView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        reg = get_object_or_404(registration, pk=pk, user=request.user)
        reg.cancelled = True
        reg.save()
        return Response({'detail': 'Cancelled'}, status=status.HTTP_200_OK)
