from django.test import TestCase
from movies.models import Movie, Genre, Director, Studio, Review
from django.urls import reverse
from django.core.files import File


class MovieListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_movies = 10
        for movie_id in range(number_of_movies):
            Movie.objects.create(
                title=f"Movie {movie_id}",
                prefix="Prefix {movie_id}",
                sub_title="Sub title {movie_id}",
                asin="1hfj12314h",
                release_date="2021-09-21",
                slug="movie-name",
                cover_image=File(
                    open(
                        "/home/hp/My_works/django/moviesapp/movies/images/mortal-kombat.jpg",
                        "rb",
                    )
                ),
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("movies"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("movies"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/movie_list.html")

    def test_amazon_url_returns_correct_asin(self):
        movie = Movie.objects.get(pk=1)
        self.assertEqual(movie.asin, movie.amazon_url)

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("movies"))
        self.assertEqual(len(response.context["movie_list"]), 10)


class MovieDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Movie.objects.create(
            title="Movie Name 1",
            prefix="Prefix",
            sub_title="Sub title",
            asin="1hfj12314h",
            release_date="2021-09-21",
            slug="movie-name-1",
            cover_image=File(
                open(
                    "/home/hp/My_works/django/moviesapp/movies/images/mortal-kombat.jpg",
                    "rb",
                )
            ),
        )

        Movie.objects.create(
            title="Movie Name 2",
            prefix="Prefix",
            sub_title="Sub title",
            asin="1hfj12314h",
            release_date="2021-09-21",
            slug="movie-name-2",
            cover_image=File(
                open(
                    "/home/hp/My_works/django/moviesapp/movies/images/mortal-kombat.jpg",
                    "rb",
                )
            ),
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/movie-name-1/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(
            reverse("movie-detail", kwargs={"slug": "movie-name-1"})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("movie-detail", kwargs={"slug": "movie-name-1"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/movie_detail.html")

    def test_view_displays_correct_movie(self):
        response = self.client.get(
            reverse("movie-detail", kwargs={"slug": "movie-name-1"})
        )
        self.assertContains(response, "Movie Name 1")
