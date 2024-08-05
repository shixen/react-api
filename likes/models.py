from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.

class Likes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


    class meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']


    def __str__(self):
        return f"{self.owner}{self.post}"