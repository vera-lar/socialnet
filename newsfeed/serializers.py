# newsfeed/serializers.py

from rest_framework import serializers
from .models import News, LiveVideo

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class LiveVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveVideo
        fields = '__all__'
