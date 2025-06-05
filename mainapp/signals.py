from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Request
from .tasks import send_request_email

@receiver(post_save, sender=Request)
def notify_new_request(sender, instance, created, **kwargs):
    if created:
        subject = f"Запрос на {instance.get_app_type_display()}"
        message = f"Тип: {instance.get_app_type_display()}\nИмя: {instance.name}\n"\
                  f"Телефон: {instance.phone}\n"\
                  f"Направление: {instance.get_case_display()}\n"\
                  f"Сообщение: {instance.message}\n"

        send_request_email.delay(subject, message, "admin@site.com", ["admin@site.com"])
