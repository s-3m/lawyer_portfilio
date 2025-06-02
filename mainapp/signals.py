from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Request
from django.core.mail import send_mail


@receiver(post_save, sender=Request)
def notify_new_request(sender, instance, created, **kwargs):
    if created:  # Если запись новая
        send_mail(
            "Запрос на звонок",
            f"Появилась новая запись: {instance}",
            "from@example.com",
            ["admin@example.com"],
            fail_silently=False,
        )
