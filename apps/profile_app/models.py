from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.full_name