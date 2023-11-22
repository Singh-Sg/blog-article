# yourappname/urls.py
from django.urls import path
from .views import ArticleListView, ArticleDetailView, ContactView, ContactSuccessView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
]
