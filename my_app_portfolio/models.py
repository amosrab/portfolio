from django.db import models


# Create your models here.

# class image

class Images(models.Model):
    alt = models.CharField(max_length=60)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.alt
