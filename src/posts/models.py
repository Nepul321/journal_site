from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.crypto import get_random_string
from users.models import CustomUser
from comments.models import Comment

def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + "-" + get_random_string(length=4)
    return unique_slug


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    image_url = models.ImageField(upload_to="media/blog-posts/header-images/%Y/%m/%d/%H/%M")
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    likes = models.ManyToManyField(CustomUser, related_name="article_likes", blank=True)
    citations = RichTextUploadingField(blank=True)
    comments = models.ManyToManyField(Comment, related_name="article_comments", blank=True)

    class Meta:
        ordering = ['-datetime', ]

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)