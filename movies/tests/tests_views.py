from django.test import TestCase
from movies.models import Movie, Genre, Director, Studio, Review
from django.urls import reverse

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
        self.assertEqual(len(response.context['movie_list']), 10)
