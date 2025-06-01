from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, "index.html")


def introduction(request):
    return render(request, "index.html")


def interest(request):
    return render(request, "index.html")


def etc(request):
    return render(request, "index.html")
