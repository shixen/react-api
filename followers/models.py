from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class followers(models.Model):
    owner = models.ForeignKey(on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    
    def __str__(self):
        return f'{self.owner}{self.followed}'
