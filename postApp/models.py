from django.db import models

# Create your models here.
class postApi(models.Model):
    name = models.CharField(max_length = 255)
    profile = models.CharField(max_length = 255)
    place = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.name)
