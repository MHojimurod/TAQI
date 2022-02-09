from rest_framework.urls import path

from myapp.views import all_news,one_news,news_category




urlpatterns = [
    path("category",news_category),
    path("news/all",all_news),
    path("news/one",one_news)
]