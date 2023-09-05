from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = "male", _("male")
    FEMALE = "female", _("female")


class RoleType(models.TextChoices):
    ACTOR = "actor", _("actor")
    DIRECTOR = "director", _("director")
    WRITER = "writer", _("writer")


class FilmworkType(models.TextChoices):
    MOVIE = "movie"
    TV_SHOW = "tv_show"
