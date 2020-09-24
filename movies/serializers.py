from rest_framework import serializers
from uuid import uuid4
from .models import MovieModel
from drf_yasg import openapi


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ['title',
                  'tagline',
                  'vote_average',
                  'vote_count',
                  'release_date',
                  'poster_path',
                  'overview',
                  'budget',
                  'revenue',
                  'genres',
                  'runtime',
                  'id']
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "Email",
            "properties": {
                "subject": openapi.Schema(
                    title="Email subject",
                    type=openapi.TYPE_STRING,
                    example="Hello"
                ),
                "body": openapi.Schema(
                    title="Email body",
                    type=openapi.TYPE_STRING,
                ),
            },
            "required": ["subject", "body"],
         }


class MovieCreateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(default=uuid4)

    class Meta:
        model = MovieModel
        fields = ['title',
                  'tagline',
                  'vote_average',
                  'vote_count',
                  'release_date',
                  'poster_path',
                  'overview',
                  'budget',
                  'revenue',
                  'genres',
                  'runtime',
                  'id']
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "Email",
            "properties": {
                "subject": openapi.Schema(
                    title="Email subject",
                    type=openapi.TYPE_STRING,
                ),
                "body": openapi.Schema(
                    title="Email body",
                    type=openapi.TYPE_STRING,
                ),
            },
            "required": ["subject", "body"],
         }

    def validate_content(self, value):
        print(self)
        for field in value:
            if bool(field) == False:
                raise serializers.ValidationError('Field could not be empty')
        return value
