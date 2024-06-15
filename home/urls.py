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

]

   
