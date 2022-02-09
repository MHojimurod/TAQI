from rest_framework.urls import path

from myapp.views import all_news,one_news




urlpatterns = [
    path("news/all",all_news),
    path("news/one",one_news)
]