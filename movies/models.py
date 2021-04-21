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


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)

    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    website = models.URLField()

    GENDER = (
        ('1', "Male"),
        ('2', "Female"),
        ('3', "Unspecified"),
    )
    gender = models.CharField(max_length=2, choices=GENDER, default='1')
