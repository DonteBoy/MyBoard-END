from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('home/', views.home,  name='home'),
    path('browser/', views.browser,  name='browser'),
    path('ai_gen/', views.ai_gen,  name='ai_gen'),
    path('3d_room/', views.three_d_room,  name='3d_room'),
    path('honors/', views.honors,  name='honors'),
]