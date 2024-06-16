from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('change_password/', views.change_password, name='change_password'),
    path('create_post/', views.create_post, name='create_post'),
    path('Profile/<str:username>/', views.Profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('community_chat/', views.community_chat, name='community_chat'),
    path('project_list/', views.project_list, name='project_list'),
    path('create_project/', views.create_project, name='create_project'),

    #community post, upcoming event and more
    path('community_posts/', views.community_posts, name='community_posts'),
    path('community_events/', views.community_events, name='community_events'),
    path('community_forum/', views.community_forum, name='community_forum'),
    path('community_forum/<int:thread_id>/', views.forum_thread, name='forum_thread'),
    path('community_tutorials/', views.community_tutorials, name='community_tutorials'),

]

   
