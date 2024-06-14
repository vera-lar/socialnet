# newsfeed/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class LiveStream(models.Model):
    # Define your fields here
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    
class Post(models.Model):
    POST_TYPES = (
        ('article', 'Article'),
        ('video', 'Video'),
        ('picture', 'Picture'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    media_url = models.URLField(blank=True, null=True)  # For video or picture URLs
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'post')

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='news_likes', blank=True)
    comments = models.ManyToManyField('Comment', related_name='news_comments', blank=True)

    def __str__(self):
        return self.title



class LiveVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    stream_url = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author.username} - {self.news.title}'
    


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title



class Post(models.Model):
    POST_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    media_url = models.URLField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Ensure this references the correct Post model
    date_liked = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
