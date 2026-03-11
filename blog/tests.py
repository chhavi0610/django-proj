from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )

    def test_create_post(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test content",
            author=self.user
        )

        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.author.username, "testuser")