from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from users.models import CustomUser

def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + "-" + get_random_string(length=4)
    return unique_slug


class Post(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(default="")
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    citations = models.TextField(blank=True)

    class Meta:
        ordering = ['-datetime', ]

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)