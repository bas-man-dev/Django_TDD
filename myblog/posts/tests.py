from django.test import TestCase
from . models import Post
# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)

    def test_string_representation(self):
        post = Post(title="My Post")
        self.assertEqual(str(post), "My Post")