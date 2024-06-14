
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import NewsViewSet, LiveVideoViewSet
from .views import go_live
from.views import LiveVideoCreateView

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'livevideos', LiveVideoViewSet)

urlpatterns = [ 
   path('newsfeed/', include(router.urls)),
   path('create/', views.create_post, name='create_post'),
   path('create_post/', views.create_post, name='create_post'), #Assuming you have a create_post view
   path('create_livevideo/', LiveVideoCreateView.as_view(), name='create_livevideo'),
   path('go_live/', go_live, name='go_live'),
   path('news/', views.news_list, name='news_list'),
   path('news/fetch/', views.fetch_news, name='fetch_news'),
]
   

     
     
    


app_name = 'newsfeed'
# newsfeed/urls.py


#router.register(r'events', EventViewSet)


#urlpatterns = [
  # path('', views.newsfeed_view, name='newsfeed'),
  #d path('dashboard/', views.dashboard, name='dashboard'),
 # path('post/new/', views.create_post, name='create_post'),
 #d path('post/<int:post_id>/', views.post_detail, name='post_detail'),
#   dpath('post/<int:post_id>/like/', views.like_post, name='like_post'),
#]