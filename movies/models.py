from django.db import models
from model_utils.models import TimeStampedModel

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


class Movie(models.Model):

    title = models.CharField(max_length=100, verbose_name="Movie Name")
    sub_title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=10)

    slug = models.SlugField(verbose_name="Movie URL Param")

    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='movies')

    asin = models.CharField(
        max_length=12, verbose_name="Amazon Standard Identification Number")
    genre = models.ManyToManyField(Genre, help_text='Genres of the movie')

    directors = models.ManyToManyField(
        Director, help_text='Directors of the movie')

    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)

    def _get_amazon_url(self):
        return self.asin

    amazon_url = property(_get_amazon_url)


class Review(TimeStampedModel):

    name = models.CharField(max_length=100, verbose_name="Reviewer name", default=None, null=True)
    text = models.CharField(max_length=512, verbose_name="Review text", default=None, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)