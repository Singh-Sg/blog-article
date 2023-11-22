# yourappname/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import BlogArticle

class AdminArticlePermissionsTest(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword', email='admin@example.com')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_admin_cannot_add_article(self):
        client = Client()
        client.login(username='admin', password='adminpassword')

        # Attempt to access the add article page
        add_article_url = reverse('admin:article_blogarticle_add')
        response = client.get(add_article_url)

        # Check that the response is a redirect (302) indicating access denied
        self.assertEqual(response.status_code, 403)

    def test_admin_can_delete_article(self):
        # Create a test article
        test_article = BlogArticle.objects.create(
            title='Test Article',
            slug='test-article',
            content='Test content',
            author=self.user,
            publish_online=True
        )

        client = Client()
        client.login(username='admin', password='adminpassword')

        # Attempt to delete the test article
        delete_article_url = reverse('admin:article_blogarticle_delete', args=[test_article.id])
        response = client.post(delete_article_url, {'post': 'yes'})

        # Check that the response is a redirect (302) indicating successful deletion
        self.assertEqual(response.status_code, 302)

        # Verify that the article has been deleted
        with self.assertRaises(BlogArticle.DoesNotExist):
            BlogArticle.objects.get(id=test_article.id)
