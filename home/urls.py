from django.urls import path
from . import views
from .views import subscribe, confirmation

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('subscribe/', subscribe, name='subscribe'),
    path('confirmation/', confirmation, name='confirmation'),
]

   
