from django.db import models


class Studio(models.Model):
    title = models.CharField(max_length=100, verbose_name="Studio Name")
    prefix = models.CharField(max_length=10)
    website = models.URLField()
    slug = models.SlugField(verbose_name="URL Param")

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name="Genre Name")
    slug = models.SlugField(verbose_name="URL Param")
