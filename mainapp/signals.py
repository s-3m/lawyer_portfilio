from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Request
from django.core.mail import send_mail


@receiver(post_save, sender=Request)
def notify_new_request(sender, instance, created, **kwargs):
    if created:  # Если запись новая
        send_mail(
            f"Запрос на {instance.get_app_type_display()}",
            f"Тип: {instance.get_app_type_display()}\nИмя: {instance.name}\n"
            f"Телефон: {instance.phone}\n"
            f"Направление: {instance.get_case_display()}\n"
            f"Сообщение: {instance.message}\n",
            "admin@admin.com",
            ("admin@example.com",),
        )
