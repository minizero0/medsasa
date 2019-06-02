from django.db import models
from django.utils import timezone

class Theme(models.Model):
    title = models.CharField(max_length=200)
    body= models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    published_at = models.DateTimeField(null=True)
    hashtags = models.ManyToManyField('Hashtag',blank=True)


class Comment(models.Model):
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="comments")
    comment_text = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_text

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
