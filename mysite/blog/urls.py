from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name="hello"),
    # url(r'^blog/$', views.blog, name="blog"),
    url(r'^blog/$', views.post_list, name="post_list"),
    url(r'^blog/post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^blog/post/new/$', views.post_new, name="post_new"),
    url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^blog/drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^blog/post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^blog/post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^time/$', views.current_datetime),  # /blog/time
]