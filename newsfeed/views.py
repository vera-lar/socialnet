
import os
import requests
from django.views import View
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from .models import News, LiveVideo, Event, Post
from .forms import NewsForm, LiveVideoForm, CommentForm
from .utils import fetch_google_news
from .forms import PostForm
from .models import Post, Event, LiveVideo
from django.contrib.auth.decorators import login_required


class NewsListView(View):
    def get(self, request):
        news_list = News.objects.all()
        return render(request, 'newsfeed/news_list.html', {'news_list': news_list})

class NewsCreateView(View):
    def get(self, request):
        form = NewsForm()
        return render(request, 'newsfeed/news_form.html', {'form': form})

    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
        return render(request, 'newsfeed/news_form.html', {'form': form})

class LiveVideoCreateView(View):
    def get(self, request):
        form = LiveVideoForm()
        return render(request, 'newsfeed/live_video_form.html', {'form': form})

    def post(self, request):
        form = LiveVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('live_video_list')
        return render(request, 'newsfeed/live_video_form.html', {'form': form})


def live_video_list(request):
    live_videos = LiveVideo.objects.all()
    return render(request, 'newsfeed/live_video.html', {'live_videos': live_videos})


def fetch_news(request):
    api_key = '265c6b7127e24e40b29040e3b461ffad'
    query = 'latest news'
    news_items = fetch_google_news(query, api_key)

    for item in news_items:
        News.objects.create(
            title=item['title'],
            content=item['content'],
            source_url=item['source_url'],
            published_date=item['published_date']
        )

    return redirect('news_list.html')


def live_video_list(request):
    return render(request, 'newsfeed/live_video.html',{})


#def newsfeed_view(request):
    posts = News.objects.all()
    events = Events.objects.all()  # Replace with actual event fetching logic
    context = {
        'posts': posts,
        'events': events,
    }
    return render(request, 'newsfeed/newsfeed_view.html', context)


def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newsfeed:news_list.html')
    else:
        form = NewsForm()
    return render(request, 'newsfeed/create_post.html', {'form': form})

def create_live_video(request):
    if request.method == 'POST':
        form = LiveVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newsfeed:live_video_list')
    else:
        form = LiveVideoForm()
    return render(request, 'newsfeed/create_live_video.html', {'form': form})

# newsfeed/views.py



class NewsListView(ListView):
    model = News
    template_name = 'newsfeed/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-published_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.fetch_events()
        return context

    def fetch_events(self):
        api_key = os.getenv('api_key')  # Ensure the API key is correctly set
        url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={api_key}'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('articles', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return []

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'newsfeed/news_form.html'
    success_url = '/newsfeed/'  # Redirect to news list view after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class LiveVideoCreateView(CreateView):
    model = LiveVideo
    form_class = LiveVideoForm
    template_name = 'newsfeed/livevideo_form.html'
    success_url = '/newsfeed/'  # Redirect to news list view after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def go_live(request):
    if request.method == 'POST':
        form = LiveVideoForm(request.POST)
        if form.is_valid():
            live_video = form.save(commit=False)
            live_video.author = request.user
            live_video.save()
            return redirect('newsfeed:news_list')
    else:
        form = LiveVideoForm()
    return render(request, 'newsfeed/go_live.html', {'form': form}) 

@login_required
def news_list(request):
    posts = Post.objects.all()
    events = Event.objects.all()
    live_videos = LiveVideo.objects.all()
    context = {
        'posts': posts,
        'events': events,
        'live_videos': live_videos,
    }
    return render(request, 'newsfeed/news_list.html', context)





def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Ensure 'news_list' is a valid URL name
    else:
        form = PostForm()

    return render(request, 'newsfeed/post_form.html', {'form': form})

def post_detail(request):
    return render(request, 'newsfeed/post_detail.html', {'Post': post_detail}


    )