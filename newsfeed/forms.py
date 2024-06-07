
# newsfeed/forms.py

from django import forms
from .models import News, LiveVideo, Comment

from .models import Post

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'author']

class LiveVideoForm(forms.ModelForm):
    class Meta:
        model = LiveVideo
        fields = ['title', 'description', 'start_time', 'stream_url', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_type', 'media_url']
