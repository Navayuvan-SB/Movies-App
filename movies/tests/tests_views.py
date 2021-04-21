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
        response = self.client.get("/movies/movie/movie-name-1/")
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


class GenreListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        number_of_genres = 10
        for genre_id in range(number_of_genres):
            Genre.objects.create(title=f"Genre {genre_id}", slug=f"genre-{genre_id}")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/genres/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/genre_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("genres"))
        self.assertEqual(len(response.context["genre_list"]), 10)


class GenreDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(title="Genre 1", slug="genre-1")
        Genre.objects.create(title="Genre 2", slug="genre-2")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/genres/genre-1/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("genre-detail", kwargs={"slug": "genre-1"}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("genre-detail", kwargs={"slug": "genre-1"}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/genre_detail.html")

    def test_view_displays_correct_movie(self):
        response = self.client.get(reverse("genre-detail", kwargs={"slug": "genre-1"}))
        self.assertContains(response, "Genre 1")


class StudioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        number_of_studios = 10
        for studio_id in range(number_of_studios):
            Studio.objects.create(
                title=f"studio {studio_id}", slug=f"studio-{studio_id}"
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/studios/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("studios"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("studios"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/studio_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("studios"))
        self.assertEqual(len(response.context["studio_list"]), 10)


class StudioDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Studio.objects.create(title="Studio 1", slug="studio-1")
        Studio.objects.create(title="Studio 2", slug="studio-2")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/studios/studio-1/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(
            reverse("studio-detail", kwargs={"slug": "studio-1"})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("studio-detail", kwargs={"slug": "studio-1"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/studio_detail.html")

    def test_view_displays_correct_movie(self):
        response = self.client.get(
            reverse("studio-detail", kwargs={"slug": "studio-1"})
        )
        self.assertContains(response, "Studio 1")


class DirectorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        number_of_directors = 10
        for director_id in range(number_of_directors):
            Director.objects.create(
                first_name=f"first director {director_id}",
                last_name=f"last director {director_id}",
                middle_name=f"middle director {director_id}",
                phone_number="9897867565",
                date_of_birth="1970-06-11",
                website="https://google.co.in",
                gender="1",
                slug=f"director-{director_id}",
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/movies/directors/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("directors"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("directors"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/director_list.html")

    def test_view_render_all_movies(self):
        response = self.client.get(reverse("directors"))
        self.assertEqual(len(response.context["director_list"]), 10)
