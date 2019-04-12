from django.db import models


# Create your models here.
class RedirectorModel(models.Model):
    original_link = models.URLField()
    id_slug = models.SlugField