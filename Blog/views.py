import time

from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {'status': ''})


