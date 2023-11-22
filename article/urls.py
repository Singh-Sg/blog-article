from django.urls import path

from .views import (
    ArticleDetailView,
    ArticleListView,
    ContactSuccessView,
    ContactView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path(
        "articles/<slug:slug>/<int:id>/",
        ArticleDetailView.as_view(),
        name="article_detail",
    ),
    path("contact/", ContactView.as_view(), name="contact"),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),

]
