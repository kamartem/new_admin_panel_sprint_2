import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.movies.enums import FilmworkType, RoleType


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(UUIDMixin, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        db_table = 'content"."genre'
        verbose_name = _("genre")
        verbose_name_plural = _("genres")

    def __str__(self):
        return self.name


class Filmwork(TimeStampedMixin):
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    creation_date = models.DateField(verbose_name=_("premiere_date"), blank=True, null=True)
    file_path = models.FileField(_("file"), blank=True, null=True, upload_to="movies/")
    rating = models.FloatField("rating", blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    type = models.CharField(_("type"), choices=FilmworkType.choices, default=FilmworkType.MOVIE)
    genres = models.ManyToManyField(Genre, through="GenreFilmwork")

    class Meta:
        db_table = 'content"."film_work'
        verbose_name = _("movie")
        verbose_name_plural = _("movies")

    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."genre_film_work'
        verbose_name = _("genre_film_work")
        verbose_name_plural = _("genre_film_works")
        unique_together = (("film_work", "genre"),)


class Person(TimeStampedMixin):
    full_name = models.CharField(_("fio"), max_length=255)

    class Meta:
        db_table = 'content"."person'
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return self.full_name


class PersonFilmwork(UUIDMixin):
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    role = models.CharField(_("role"), max_length=255, choices=RoleType.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content"."person_film_work'
        verbose_name = _("person_film_work")
        verbose_name_plural = _("person_film_works")
        unique_together = (("film_work", "person", "role"),)
