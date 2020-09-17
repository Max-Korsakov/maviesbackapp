from rest_framework import serializers
from uuid import uuid4
from .models import MovieModel


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

    def validate_content(self, value):
        print(self)
        for field in value:
            if bool(field) == False:
                raise serializers.ValidationError('Field could not be empty')
        return value
