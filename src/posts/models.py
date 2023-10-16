from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    citations = models.TextField(blank=True)

    class Meta:
        ordering = ['-datetime', ]

    def __str__(self):
        return str(self.id)