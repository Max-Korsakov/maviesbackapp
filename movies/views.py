from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import MovieSerializer, MovieCreateSerializer
from .models import MovieModel


@api_view(['GET'])
@permission_classes([AllowAny])
def moovie_list_view(request, *args, **kwargs):
    qs = MovieModel.objects.all()
    if request.query_params and request.query_params['offset']:
        OFFSET = int(request.query_params['offset'])
    else:
        OFFSET = 0
    if request.query_params and request.query_params['limit']:
        LIMIT = int(request.query_params['limit'])
    else:
        LIMIT = 12
    if request.query_params and request.query_params['filter']:
        qs = qs.filter(genres__contains=request.query_params['filter'])
    if request.query_params and request.query_params['sortBy'] and request.query_params['sortOrder']:
        if request.query_params['sortOrder'] == 'desc':
            qs = qs.order_by('-' + request.query_params['sortBy'])
        elif request.query_params['sortOrder'] == 'asc':
            qs = qs.order_by(request.query_params['sortBy'])
    if request.query_params and request.query_params['search']:
        qs = qs.filter(title__contains=request.query_params['search'])
    data = qs[OFFSET:OFFSET + LIMIT]
    serializer = MovieSerializer(data, many=True)
    content = {'movie_count': qs.count(), 'data': serializer.data}
    return Response(content)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_movie(request, *args, **kwargs):
    data = request.data or None
    serializer = MovieCreateSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_movie(request, *args, **kwargs):
    qs = MovieModel.objects.filter(id=request.data['id'])
    data = request.data or None
    obj = qs.first()
    serializer = MovieCreateSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.update(obj, data)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_movie(request, *args, **kwargs):
    qs = MovieModel.objects.filter(id=request.data['id'])
    if not qs.exists():
        return Response({"message": "Movie was not found"}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Movie was deleted"}, status=200)
