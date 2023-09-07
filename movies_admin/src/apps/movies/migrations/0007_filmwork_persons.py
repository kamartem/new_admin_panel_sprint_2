# Generated by Django 4.2.5 on 2023-09-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_rename_created_filmwork_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='persons',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.person'),
        ),
    ]
