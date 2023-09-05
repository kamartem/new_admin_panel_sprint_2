from django.urls import include, path

urlpatterns = [
    path('v1/', include('apps.movies.api.v1.urls')),
]
