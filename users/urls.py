from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

from .views import change_password



#urlpatterns = [
   # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
   # path('signup/', views.signup, name='signup'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#]

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    
]





   
    # Other URL patterns...