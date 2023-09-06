from rest_framework import serializers

from apps.movies.models import Filmwork


class FilmworkSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)
    directors = serializers.StringRelatedField(many=True, read_only=True)
    screenwriters = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Filmwork
        fields = [
            "id",
            "title",
            "description",
            "creation_date",
            "rating",
            "type",
            "genres",
            "actors",
            "directors",
            "screenwriters",
        ]
