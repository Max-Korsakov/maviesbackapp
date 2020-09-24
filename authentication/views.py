from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

@swagger_auto_schema(method='post', operation_description='This endpoint does some magic', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }
))
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request, *args, **kwargs):
    user = request.data
    serializer = RegisterSerializer(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    user_data = serializer.data

    return Response(user_data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request, *args, **kwargs):
    user = request.data
    serializer = LoginSerializer(data=user)
    serializer.is_valid(raise_exception=True)
    user_data = serializer.data
    return Response(user_data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, *args, **kwargs):
    qs = User.objects.filter(email=request.data['email'])
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({"message": "User was deleted"}, status=200)
