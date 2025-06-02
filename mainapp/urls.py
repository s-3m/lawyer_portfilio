from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mainapp import views

app_name = "mainapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact_request/", views.RequestCreateView.as_view(), name="contact_request"),
    path("success_request/", views.SuccessRequest.as_view(), name="success_request"),
]
