# Generated by Django 4.1.4 on 2022-12-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bookID", models.IntegerField()),
                ("title", models.CharField(max_length=500)),
                ("authors", models.CharField(max_length=500)),
                ("average_rating", models.FloatField()),
                ("isbn", models.CharField(max_length=10)),
                ("isbn13", models.IntegerField()),
                ("language_code", models.CharField(max_length=6)),
                ("num_pages", models.IntegerField()),
                ("ratings_count", models.IntegerField()),
                ("text_reviews_count", models.IntegerField()),
                ("publication_date", models.DateTimeField()),
                ("publisher", models.CharField(max_length=255)),
            ],
        ),
    ]
