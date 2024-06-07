# newsfeed/api_views.py

# newsfeed/api_views.py

from rest_framework import viewsets
from .models import News, LiveVideo
from .serializers import NewsSerializer, LiveVideoSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class LiveVideoViewSet(viewsets.ModelViewSet):
    queryset = LiveVideo.objects.all()
    serializer_class = LiveVideoSerializer
