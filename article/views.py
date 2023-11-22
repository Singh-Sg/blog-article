from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import BlogArticle, ContactRequest


class HomeView(View):
    def get(self, request):
        return render(request, 'base.html', {})


class ArticleListView(ListView):
    model = BlogArticle
    template_name = "articles/list.html"
    context_object_name = "articles"
    paginate_by = 2
    ordering = ["-pk"]


class ArticleDetailView(DetailView):
    model = BlogArticle
    template_name = "articles/detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_list_url"] = reverse_lazy("article_list")
        return context


class ContactView(FormView):
    template_name = "contact/form.html"
    form_class = ContactForm

    def form_valid(self, form):
        ContactRequest.objects.create(
            email=form.cleaned_data["email"],
            name=form.cleaned_data["name"],
            content=form.cleaned_data["content"],
        )

        # Send email to debug@mir.de
        email_subject = "New Contact Request"
        email_body = (
            f"Name: {form.cleaned_data['name']}\n"
            f"Email: {form.cleaned_data['email']}\n"
            f"Content: {form.cleaned_data['content']}"
        )

        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["debug@mir.de"],
            reply_to=[form.cleaned_data["email"]],
        )

        email_message.send(fail_silently=False)
        self.success_url = reverse_lazy("contact_success",)

        return super().form_valid(form)


class ContactSuccessView(View):
    template_name = 'contact/success.html'

    def get(self, request):
        return render(request, self.template_name, {
            'message' : 'Contact Request has been submitted successfully',
            })
