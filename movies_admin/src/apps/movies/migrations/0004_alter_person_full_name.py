# Generated by Django 4.2.3 on 2023-07-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_person_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="full_name",
            field=models.CharField(max_length=255, verbose_name="fio"),
        ),
    ]
