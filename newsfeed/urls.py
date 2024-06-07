
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import NewsViewSet, LiveVideoViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'livevideos', LiveVideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.create_post, name='create_post'),
    path('create_post/', views.create_post, name='create_post'),  # Assuming you have a create_post view
    path('news_list/', views.create_post, name='news_list'),  # Assuming you have a create_post view

]


app_name = 'newsfeed'
# newsfeed/urls.py


#router.register(r'events', EventViewSet)


#urlpatterns = [
    #path('', include(router.urls)),
   # path('news/', NewsListView.as_view(), name='news_list'),
   #  path('news/fetch/', views.fetch_news, name='fetch_news'),
   # path('news/create/', NewsCreateView.as_view(), name='news_create'),
    #path('live/create/', LiveVideoCreateView.as_view(), name='live_video_create'),
 #   path('live/', live_video_list, name='live_video_list'),
    #path('live/go/', go_live, name='go_live'),
#]



#urlpatterns = [
   # path('', NewsListView.as_view(), name='news_list'),
    #path('create_news/', NewsCreateView.as_view(), name='create_news'),
   # path('create_livevideo/', LiveVideoCreateView.as_view(), name='create_livevideo'),
    #path('go_live/', go_live, name='go_live'),
   # path('news/', views.news_list, name='news_list'),
   # path('news/fetch/', views.fetch_news, name='fetch_news'),
#]

#urlpatterns = [
  # path('', views.newsfeed_view, name='newsfeed'),
   # path('dashboard/', views.dashboard, name='dashboard'),
  #  path('post/new/', views.create_post, name='create_post'),
  # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    #path('post/<int:post_id>/like/', views.like_post, name='like_post'),
#]