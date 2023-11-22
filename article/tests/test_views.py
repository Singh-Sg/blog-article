from article.models import BlogArticle

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ArticleListViewTest(TestCase):
    def test_article_list_view_status_code(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)

    def test_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse("article_list"))
        self.assertTemplateUsed(response, "articles/list.html")


class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.blog_article = BlogArticle.objects.create(
            title="Test Title",
            slug="test-title",
            content="Test content",
            author=self.user,
            publication_datetime="2023-01-01 12:00:00",
            publish_online=True,
        )

    def test_article_detail_view_status_code(self):
        response = self.client.get(
            reverse(
                "article_detail",
                kwargs={"slug": self.blog_article.slug, "id": self.blog_article.id},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_article_detail_view_uses_correct_template(self):
        response = self.client.get(
            reverse(
                "article_detail",
                kwargs={"slug": self.blog_article.slug, "id": self.blog_article.id},
            )
        )
        self.assertTemplateUsed(response, "articles/detail.html")


class ContactViewTest(TestCase):
    def test_contact_view_status_code(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_uses_correct_template(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact/form.html")

    def test_contact_form_submission(self):
        response = self.client.post(
            reverse("contact"),
            data={
                "email": "test@example.com",
                "name": "Test Name",
                "content": "Test content",
            },
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirect after successful form submission


class ContactSuccessViewTest(TestCase):
    def test_contact_success_view_status_code(self):
        response = self.client.get(reverse("contact_success"))
        self.assertEqual(response.status_code, 200)

    def test_contact_success_view_uses_correct_template(self):
        response = self.client.get(reverse("contact_success"))
        self.assertTemplateUsed(response, "contact/success.html")
