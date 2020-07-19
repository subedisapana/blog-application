
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader


def homepage(request):
    return render(request, 'homepage.html', {'status': ''})


def blog(request):
    return render(request, 'blog.html', {'status': ''})


def create(request):
    return render(request, 'create.html', {'status': ''})


