from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Text = models.TextField()
    Likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.Author} - {self.Title} - {self.Likes}"
