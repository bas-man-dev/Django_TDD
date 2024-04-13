from django.test import TestCase
from . models import Post
from http import HTTPStatus
# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)

    def test_string_representation(self):
        post = Post(title="My Post")
        self.assertEqual(str(post), "My Post")

class HomeViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title="My  First Post", body="My Post Body")
        Post.objects.create(title="My  Second Post", body="My Second Post Body")

    def test_home_view_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)