from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from .views import dashboard


urlpatterns = [
   
    path('', dashboard, name='dashboard'),  
    path('create_profile/', views.create_profile, name='create_profile'),
    path('setprofile/', views.setprofile, name='setprofile'),
    path('users/', views.login, name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('profile/', views.profile, name='profile'),  # Assuming you have a profile view
    path('create_post/', views.create_post, name='create_post'), 
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Assuming you have an edit_profile view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]
