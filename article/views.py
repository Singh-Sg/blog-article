from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from .forms import ContactForm
from .models import BlogArticle


class HomeView(View):
    def get(self, request):
        return render(request, "base.html", {})


class ArticleListView(ListView):
    model = BlogArticle
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 5
    ordering = ["-pk"]


class ArticleDetailView(DetailView):
    model = BlogArticle
    template_name = "articles/detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list_url"] = reverse_lazy("article_list")
        return context


class ContactView(CreateView):
    template_name = "contact/form.html"
    form_class = ContactForm
    success_url = reverse_lazy(
        "contact_success",
    )


class ContactSuccessView(View):
    template_name = "contact/success.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            {
                "message": "Contact Request has been submitted successfully",
            },
        )
