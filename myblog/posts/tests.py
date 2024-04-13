from django.test import TestCase

# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)