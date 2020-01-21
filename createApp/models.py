from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    href = models.URLField(max_length=250)
    ingredients = models.CharField(max_length=255, blank=True,null=True)
    thumbnail = models.URLField(max_length=250,blank=True,null=True)

    def __str__(self):
        return str(self.title)