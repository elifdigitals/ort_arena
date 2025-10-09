from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema 
from authUser import serializers, permissions
from rest_framework.authtoken.models import Token
from .models import CustomUser

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=serializers.UserSerializer,
        responses={201: {"message": "User created successfully, please confirm registration"}},
        tags=["Register"],
    )
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully, please confirm registration"}, 
                            status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=serializers.UserSerializer,
        responses={200: {"token": "string", "user_id": "integer", "email": "string"}},
        tags=["Login"],
    )
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Successfully login"}, status=status.HTTP_201_CREATED)

        return Response({"error": "400_BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: serializers.UserSerializer},
        tags=["Current User"],
    )
    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })

    @extend_schema(
        request=serializers.UserSerializer,
        responses={200: {"message": "User updated successfully"}},
        tags=["Current User"],
    )
    def put(self, request):
        user = request.user
        serializer = serializers.UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
