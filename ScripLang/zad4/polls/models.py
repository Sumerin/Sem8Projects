from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os


def get_image_path(instance, filename):
    return os.path.join(str(instance.id), filename)

# Create your models here.


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.TimeField(default=timezone.now)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_posted = models.TimeField(default=timezone.now)
    content = models.TextField()
