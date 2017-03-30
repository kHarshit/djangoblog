from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.utils import timezone
import datetime
from .forms import PostForm


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


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect('post_detail', pk=post.pk)
            # return HttpResponseRedirect('/thanks/')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return HttpResponseRedirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now {0}".format(now)
    return HttpResponse(html)

