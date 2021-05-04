import socket

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def main(request):
    hostname = socket.gethostname()
    return render(request, 'index.html', locals())


def stats(request):
    hostname = socket.gethostname()
    return render(request, 'covidstats.html', locals())
