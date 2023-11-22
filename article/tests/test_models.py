from article.models import BlogArticle

from django.contrib.auth.models import User
from django.test import TestCase


class BlogArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_blog_article_creation(self):
        blog_article = BlogArticle.objects.create(
            title="Test Title",
            slug="test-title",
            content="Test content",
            author=self.user,
            publication_datetime="2023-01-01 12:00:00",
            publish_online=True,
        )
        self.assertEqual(str(blog_article), "Test Title")
        self.assertEqual(blog_article.slug, "test-title")
        self.assertEqual(blog_article.author, self.user)
