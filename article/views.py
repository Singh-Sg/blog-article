# yourappname/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import BlogArticle, ContactRequest
from .forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage


class ArticleListView(ListView):
    model = BlogArticle
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 2
    ordering = ['-pk'] 


class ArticleDetailView(DetailView):
    model = BlogArticle
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list_url'] = reverse_lazy('article_list')
        return context


class ContactView(FormView):
    template_name = 'contact/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        # Save the contact request to the database
        ContactRequest.objects.create(
            email=form.cleaned_data['email'],
            name=form.cleaned_data['name'],
            content=form.cleaned_data['content']
        )

        # Send email to debug@mir.de
        email_subject = 'New Contact Request'
        email_body = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nContent: {form.cleaned_data['content']}"

        email_message = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['debug@mir.de'],
            reply_to=[form.cleaned_data['email']]  # Adding Reply-To header
        )

        email_message.send(fail_silently=False)

        return super().form_valid(form)


class ContactSuccessView(ListView):
    model = ContactRequest
    template_name = 'contact/success.html'
    context_object_name = 'contact_requests'
    paginate_by = 5
    ordering = ['-date'] 