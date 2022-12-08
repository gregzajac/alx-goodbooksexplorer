from django.db import models
from django.utils import timezone


# Create your models here.

class Bio(models.Model):
    content = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    b_year = models.PositiveIntegerField()
    bio = models.OneToOneField(Bio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return timezone.now().year - self.b_year


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField("posts.Tag", related_name="posts", blank=True)
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.author})"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name