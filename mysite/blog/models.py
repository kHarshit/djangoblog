from django.db import models
from django.utils import timezone


class Post(models.Model):  # name of model  # models.Model means that the Post is a Django Model,
    #  so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User')  # link to another model
    title = models.CharField(max_length=200)  # text with a limited number of characters
    text = models.TextField()  # long text without a limit.
    create_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)  # error

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text






