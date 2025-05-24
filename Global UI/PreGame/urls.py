from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_page, name='scan_page'),
    path('video_feed/', views.video_feed, name='video_feed'),
]