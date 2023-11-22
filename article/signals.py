from article.models import ContactRequest

from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver


SEND_MAIL_TO = ["debug@mir.de"]


@receiver(post_save, sender=ContactRequest)
def contact_request_created(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            "Contact Request",
            f"Name: {instance.name}\n{instance.content}",
            settings.DEFAULT_FROM_EMAIL,
            SEND_MAIL_TO,
            reply_to=[instance.email],
        )
        email.send()
