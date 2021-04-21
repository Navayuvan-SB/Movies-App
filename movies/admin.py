from django.contrib import admin
from .models import Movie, Studio, Genre, Review, Director


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 2


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title", "prefix")
    inlines = [ReviewInline]


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ("title", "prefix")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "website")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "text", "movie")
