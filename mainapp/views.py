from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from mainapp.forms import RequestForm
from mainapp.models import Request


# Create your views here.


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class RequestCreateView(CreateView):
    model = Request
    template_name = "mainapp/request.html"
    form_class = RequestForm
    success_url = reverse_lazy("mainapp:index")
