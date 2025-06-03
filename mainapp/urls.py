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
    path("create_review/", views.ReviewCreateView.as_view(), name="create_review"),
    path("success_review/", views.SuccessReview.as_view(), name="success_review"),
    path("review_list/", views.ReviewListView.as_view(), name="review_list"),
]
