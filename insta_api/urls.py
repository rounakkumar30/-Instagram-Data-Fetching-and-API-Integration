from django.urls import path
from .views import fetch_instagram_post, fetch_instagram_post_scrape

urlpatterns = [
    path('', fetch_instagram_post, name='fetch_post'),
    path('fetch_scrape/', fetch_instagram_post_scrape, name='fetch_scrape'),
]
