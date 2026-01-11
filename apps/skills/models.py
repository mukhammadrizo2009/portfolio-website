from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="skills/")
    level = models.CharField(
        max_length=20,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ]
    )

    def __str__(self):
        return self.name