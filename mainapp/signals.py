from django.db.models.signals import post_save
from django.dispatch import receiver
from mainapp.models import Request, Review
from .tasks import send_email_notify

@receiver(post_save, sender=Request)
def notify_new_request(sender, instance, created, **kwargs):
    if created:
        subject = f"Запрос на {instance.get_app_type_display()}"
        message = (f"Тип: {instance.get_app_type_display()}\n"
                   f"Имя: {instance.name}\n"
                   f"Регион: {instance.get_region_display()}\n"
                   f"Телефон: {instance.phone}\n"
                   f"Направление: {instance.get_case_display()}\n"
                   f"Сообщение: {instance.message}\n")

        send_email_notify.delay(subject, message, "admin@site.com", ["admin@site.com"])


@receiver(post_save, sender=Review)
def notify_new_review(sender, instance: Review, created, **kwargs):
    if created:
        subject = f"Новый отзыв"
        message = ("Новый отзыв ожидает модерации. Отзыв не появится на сайте, пока не пройдёт вашу модерацию!\n"
                   f"Отзыв:\n{instance.text}\n"
                   f"От: {instance.name}\n"
                   f"Направление: {instance.get_case_display()}\n")


        send_email_notify.delay(subject, message, "admin@site.com", ["admin@site.com"])
