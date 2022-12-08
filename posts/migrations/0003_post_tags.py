# Generated by Django 4.1.4 on 2022-12-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(related_name="posts", to="posts.tag"),
        ),
    ]