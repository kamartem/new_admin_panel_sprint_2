from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from config.components.common import PAGE_COUNT
from movies.models import Filmwork, Role


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    @staticmethod
    def get_person_aggregation(role: Role) -> ArrayAgg:
        return ArrayAgg(
            'persons__full_name',
            distinct=True,
            filter=Q(personfilmwork__role=role)
        )

    def get_queryset(self):
        queryset = MoviesApiMixin.model.objects \
            .values().annotate(
                genres=ArrayAgg('genres__name', distinct=True),
                actors=self.get_person_aggregation(Role.ACTOR),
                directors=self.get_person_aggregation(Role.DIRECTOR),
                writers=self.get_person_aggregation(Role.WRITER)
            )
        return queryset

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = PAGE_COUNT

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        _next = page.next_page_number() if page.has_next() else None
        _prev = page.previous_page_number() if page.has_previous() else None
        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': _prev,
            'next': _next,
            'results': list(queryset.values()),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):

    def get_context_data(self, **kwargs):
        return kwargs['object']
