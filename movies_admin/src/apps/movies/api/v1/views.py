from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from rest_framework import generics

from apps.movies.api.v1.serializers import FilmworkSerializer
from apps.movies.enums import RoleType
from apps.movies.models import Filmwork


class MoviesListApiViewMixin:
    queryset = (
        Filmwork.objects.prefetch_related(
            'genres',
            'persons',
        )
        .values()
        .all()
        .annotate(
            genres=ArrayAgg('genres__name', distinct=True),
            actors=ArrayAgg(
                'persons__full_name',
                filter=Q(personfilmwork__role__icontains=RoleType.ACTOR),
                distinct=True,
            ),
            directors=ArrayAgg(
                'persons__full_name',
                filter=Q(personfilmwork__role__icontains=RoleType.DIRECTOR),
                distinct=True,
            ),
            writers=ArrayAgg(
                'persons__full_name',
                filter=Q(personfilmwork__role__icontains=RoleType.WRITER),
                distinct=True,
            ),
        )
    )
    serializer_class = FilmworkSerializer


class MoviesListApi(MoviesListApiViewMixin, generics.ListAPIView):
    pass


class MoviesDetailApi(MoviesListApiViewMixin, generics.RetrieveAPIView):
    pass
