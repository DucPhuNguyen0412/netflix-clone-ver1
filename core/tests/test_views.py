from moto import mock_s3
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Movie
from django.core.files.uploadedfile import SimpleUploadedFile
import boto3
import botocore

MY_BUCKET = "mytestbucket"

@mock_s3
class ViewTestCase(TestCase):

    def setUp(self):
        # Setup client and user
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        # Setup mock S3
        client = boto3.client(
            "s3",
            region_name="us-east-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        try:
            s3 = boto3.resource(
                "s3",
                region_name="us-east-1",
                aws_access_key_id="fake_access_key",
                aws_secret_access_key="fake_secret_key",
            )
            s3.meta.client.head_bucket(Bucket=MY_BUCKET)
        except botocore.exceptions.ClientError:
            pass
        else:
            err = f"{MY_BUCKET} should not exist."
            raise EnvironmentError(err)
        client.create_bucket(Bucket=MY_BUCKET)

        # Create test movie
        dummy_file_content = b"dummy content"
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
        
        # Print the uu_id of the movie to check its format
        print(f"Created movie UUID in test setup: {self.movie.uu_id}")

    def tearDown(self):
        # Clean up mock S3 bucket
        s3 = boto3.resource(
            "s3",
            region_name="us-east-1",
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        bucket = s3.Bucket(MY_BUCKET)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
        super().tearDown()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        print("Tested index view.")

    def test_movie_view(self):
        response = self.client.get(reverse('movie', args=[self.movie.uu_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie.html')
        print("Tested movie view.")

    def test_genre_view(self):
        response = self.client.get(reverse('genre', args=['action']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre.html')
        print("Tested genre view.")

    def test_my_list_view(self):
        response = self.client.get(reverse('my-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_list.html')
        print("Tested my list view.")

    def test_login_view_redirect(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        print("Tested login view redirect.")
