from django.shortcuts import render
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("hello, world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now {0}".format(now)
    return HttpResponse(html)

