from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from core.models import Movie, MovieList
import datetime

class MovieModelTest(TestCase):
    
    def setUp(self):
        # Create a sample movie
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description.",
            release_date=datetime.date.today(),
            genre="action",
            length=120,
            image_card="path/to/image_card.jpg",
            image_cover="path/to/image_cover.jpg",
            video="path/to/video.mp4",
            movie_views=0
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "A test movie description.")
        self.assertEqual(self.movie.genre, "action")

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")

    def test_invalid_data(self):
        # Test creation of a movie with invalid data
        movie = Movie(
            title="",
            description="",
            # Provide other fields with invalid data
        )
        with self.assertRaises(ValidationError):
            movie.full_clean()  # This should raise ValidationError

class MovieListModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description.",
            release_date=datetime.date.today(),
            genre="action",
            length=120,
            image_card="path/to/image_card.jpg",
            image_cover="path/to/image_cover.jpg",
            video="path/to/video.mp4",
            movie_views=0
        )
        self.movie_list = MovieList.objects.create(
            owner_user=self.user,
            movie=self.movie
        )

    def test_movie_list_creation(self):
        self.assertEqual(self.movie_list.owner_user, self.user)
        self.assertEqual(self.movie_list.movie, self.movie)

    def test_movie_list_str(self):
        expected_str = f"{self.user.username}'s list - {self.movie.title}"
        self.assertEqual(str(self.movie_list), expected_str)
