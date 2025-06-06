from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from mainapp.forms import RequestForm, ReviewForm
from mainapp.models import Request, Review


# Create your views here.


class IndexView(TemplateView):
    template_name = "mainapp/index.html"
    extra_context = {"title": "Судебная защита в Москве"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews_list"] = Review.objects.filter(approved=True)[:10]
        return context


class RequestCreateView(CreateView):
    model = Request
    template_name = "mainapp/request.html"
    form_class = RequestForm
    success_url = reverse_lazy("mainapp:success_request")

    def get_initial(self, **kwargs):
        initial = super().get_initial()
        if self.kwargs.get("req_type") == "meet":
            initial["app_type"] = "MEET"  # установите новое значение
        return initial


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
    paginate_by = 6
    queryset = Review.objects.filter(approved=True)


class ContactsView(TemplateView):
    template_name = "mainapp/contacts.html"
    extra_context = {"active_contact": "active"}
