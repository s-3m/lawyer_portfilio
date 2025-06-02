from django.contrib import admin

from mainapp.models import Request, Review


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "case",
        "region",
        "app_type",
        "message",
        "created_at",
    )
    list_filter = ("created_at", "region", "case", "app_type")
    readonly_fields = ("created_at",)


@admin.register(Review)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "case",
        "text",
        "created_at",
        "updated_at",
        "approved",
    )
    list_filter = ("created_at", "name", "case", "approved")
    readonly_fields = ("created_at",)
