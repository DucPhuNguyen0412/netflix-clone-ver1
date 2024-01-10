from moto import mock_s3
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Movie
from django.core.files.uploadedfile import SimpleUploadedFile
import boto3

@mock_s3
class ViewTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.setUpMockedS3()

    @classmethod
    def setUpMockedS3(cls):
        with mock_s3():
            # Create a mock S3 bucket
            s3 = boto3.client('s3', region_name='us-east-1')
            s3.create_bucket(Bucket='mytestbucket')

    def setUp(self):
        # Create a client to make requests
        self.client = Client()

        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Dummy file content
        dummy_file_content = b"dummy content"

        # Create a test movie with dummy image and video files
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date="2021-01-01",
            genre="action",
            length=120,
            movie_views=0,
            image_card=SimpleUploadedFile("image_card.jpg", dummy_file_content, content_type="image/jpeg"),
            image_cover=SimpleUploadedFile("image_cover.jpg", dummy_file_content, content_type="image/jpeg"),
            video=SimpleUploadedFile("video.mp4", dummy_file_content, content_type="video/mp4")
        )

    def tearDown(self):
        super().tearDown()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_movie_view(self):
        response = self.client.get(reverse('movie', args=[self.movie.uu_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie.html')

    def test_genre_view(self):
        response = self.client.get(reverse('genre', args=['action']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre.html')

    def test_my_list_view(self):
        response = self.client.get(reverse('my-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_list.html')

    def test_login_view_redirect(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
