from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Request(models.Model):

    CASE_CHOICES = (
        ("1", "Банкротство"),
        ("2", "Cемейные споры"),
        ("3", "Проблемы с ГИБДД"),
        ("4", "Судебные приставы"),
    )

    APP_TYPE_CHOICES = (
        ("CALL", "Заявка на консультацию"),
        ("MEET", "Запись на приём"),
    )

    REGION_CHOICES = (
        ("M", "Москва"),
        ("MO", "Московская область"),
        ("K", "Калининград"),
    )

    name = models.CharField(max_length=100, verbose_name="Имя", blank=False, null=False)
    phone = PhoneNumberField(
        verbose_name="Номер телефона",
        region="RU",  # Автоматическая валидация для России
        blank=False,
        null=False,
        error_messages={
            "invalid": "Введите телефон в формате 89165556677.",
        },
    )
    case = models.CharField(
        verbose_name="Направление",
        max_length=20,
        blank=False,
        null=False,
        choices=CASE_CHOICES,
        default="1",
    )
    region = models.CharField(
        verbose_name="Регион", max_length=2, choices=REGION_CHOICES, default="M"
    )
    app_type = models.CharField(
        verbose_name="Тип заявки",
        max_length=4,
        choices=APP_TYPE_CHOICES,
        default="CALL",
    )
    message = models.TextField(
        verbose_name="Сообщение",
        blank=True,
        null=True,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    processed = models.BooleanField(verbose_name="Заявка обработана", default=False)
    comment = models.TextField(verbose_name="Комментарий", blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запрос"  # Единственное число
        verbose_name_plural = "Запросы"  # Множественное число


class Review(models.Model):
    CASE_CHOICES = (
        ("1", "Банкротство"),
        ("2", "Cемейные споры"),
        ("3", "Проблемы с ГИБДД"),
        ("4", "Судебные приставы"),
    )
    name = models.CharField(max_length=40, verbose_name="Имя", blank=False, null=False)
    case = models.CharField(
        verbose_name="Направление",
        max_length=20,
        blank=False,
        null=False,
        choices=CASE_CHOICES,
        default="3",
    )
    text = models.TextField(verbose_name="Отзыв", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    approved = models.BooleanField(verbose_name="Модерация", default=False)

    class Meta:
        verbose_name = "Отзыв"  # Единственное число
        verbose_name_plural = "Отзывы"  # Множественное число
