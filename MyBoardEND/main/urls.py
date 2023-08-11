from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('home/', views.home,  name='home'),
    path('news/', views.home,  name='news'),
    path('ai_gen/', views.home,  name='ai_gen'),
    path('3d_room/', views.home,  name='3d_room'),
    path('honors/', views.home,  name='honors'),
]