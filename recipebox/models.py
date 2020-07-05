from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def url(self):
        return self.name.replace(" ", "_").lower()


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length = 20)
    instructions = models.TextField()

    def __str__(self):
        return self.title
    
    def url(self):
        return self.title.replace(" ", "_").lower()
