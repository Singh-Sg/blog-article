from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BlogArticle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_datetime = models.DateTimeField(auto_now=True)
    publish_online = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Blog Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ContactRequest(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Request from {self.name} ({self.email})"

    class Meta:
        verbose_name_plural = "ContactRequests"
