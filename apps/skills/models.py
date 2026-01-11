from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(help_text="0-100")
    
    def __str__(self):
        return self.name