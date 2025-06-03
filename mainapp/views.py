from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from mainapp.forms import RequestForm, ReviewForm
from mainapp.models import Request, Review


# Create your views here.


class IndexView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews_list"] = Review.objects.filter(approved=True)[:10]
        return context


class RequestCreateView(CreateView):
    model = Request
    template_name = "mainapp/request.html"
    form_class = RequestForm
    success_url = reverse_lazy("mainapp:success_request")


class SuccessRequest(TemplateView):
    template_name = "mainapp/request_success.html"


class PageNotFound(TemplateView):
    template_name = "mainapp/404.html"


class ReviewCreateView(CreateView):
    model = Review
    template_name = "mainapp/add_review.html"
    form_class = ReviewForm
    success_url = reverse_lazy("mainapp:success_review")


class SuccessReview(TemplateView):
    template_name = "mainapp/review_success.html"


class ReviewListView(ListView):
    model = Review
    template_name = "mainapp/review_list.html"
    context_object_name = "reviews"
    extra_context = {"class_active": "active"}
