from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import MovieSerializer, MovieCreateSerializer
from .models import MovieModel

test_param = [openapi.Parameter(
    'sortBy', openapi.IN_QUERY, description="Field to sort by", type=openapi.TYPE_STRING),
    openapi.Parameter(
    'sortOrder', openapi.IN_QUERY, description="Value to define sort direction - 'desc' or 'asc'", type=openapi.TYPE_STRING),
     openapi.Parameter(
    'search', openapi.IN_QUERY, description="Search value", type=openapi.TYPE_STRING),
     openapi.Parameter(
    'searchBy', openapi.IN_QUERY, description="Type of search (title or genres)", type=openapi.TYPE_STRING),
     openapi.Parameter(
    'filter', openapi.IN_QUERY, description="Array to filter by genres", type=openapi.TYPE_STRING),
    openapi.Parameter(
    'offset', openapi.IN_QUERY, description="Offset in result array for pagination", type=openapi.TYPE_STRING),
    openapi.Parameter(
    'limit', openapi.IN_QUERY, description="Limit amount of items in result array for pagination", type=openapi.TYPE_STRING),
    ]
user_response = openapi.Response('Movies list', MovieSerializer)

@swagger_auto_schema(method='get', operation_description='Get movies list', manual_parameters=test_param, responses={200: user_response})
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

@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_by_id(request,id, *args, **kwargs):
    qs=MovieModel.objects.get(id=id)
    serializer = MovieSerializer(qs)
    content = {'data': serializer.data}
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_movie(request, *args, **kwargs):
    print('request=>', request.data)
    qs = MovieModel.objects.filter(id=request.data['id'])
    if not qs.exists():
        return Response({"message": "Movie was not found"}, status=404)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Movie was deleted"}, status=200)
