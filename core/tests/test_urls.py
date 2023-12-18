from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import index, login, signup, logout, movie, genre, my_list, add_to_list, search

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

    def test_movie_url_is_resolved(self):
        url = reverse('movie', args=['some-uuid'])
        self.assertEqual(resolve(url).func, movie)

    def test_genre_url_is_resolved(self):
        url = reverse('genre', args=['some-genre'])
        self.assertEqual(resolve(url).func, genre)

    def test_my_list_url_is_resolved(self):
        url = reverse('my-list')
        self.assertEqual(resolve(url).func, my_list)

    def test_add_to_list_url_is_resolved(self):
        url = reverse('add-to-list')
        self.assertEqual(resolve(url).func, add_to_list)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)
