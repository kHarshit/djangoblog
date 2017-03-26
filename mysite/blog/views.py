from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
import datetime


def hello(request):
    return HttpResponse("hello, world")


def blog(request):
    return HttpResponse("This is the blog.")


def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now {0}".format(now)
    return HttpResponse(html)

