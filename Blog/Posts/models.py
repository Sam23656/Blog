from django.db import models


# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name}"


class Post(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Text = models.TextField()
    Likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.Author} - {self.Title} - {self.Likes}"
