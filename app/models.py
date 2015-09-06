from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):

    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255,)
    # profile_pic = models.ImageField(upload_to='pictures', blank=True)
    email = models.EmailField()

    def __str__(self):
        return ' '.join([self.first_name, self.last_name, ])


class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True)
    about = models.CharField(max_length=140)
    website = models.URLField(max_length=140)
    reputation = models.IntegerField(default=1)

    def __str__(self):
        return 'Profile of user : %s' % self.user.username


class Articles(models.Model):

    description = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    uploader = models.ForeignKey(User)
    time_stamp = models.DateTimeField()
    votes = models.PositiveIntegerField(default=1)

class Like(models.Model):

    user = models.ForeignKey(User)
    article = models.ForeignKey(Articles)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):

    user = models.ForeignKey(User)
    article = models.ForeignKey(Articles)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=150,)

class News(models.Model):

    text = models.CharField(max_length=255,)
    link = models.URLField(max_length=255,)
    timestamp = models.CharField(max_length=20,)

class NewsContent(models.Model):

    content = models.TextField()

class ContactUs(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.CharField(max_length=255)
