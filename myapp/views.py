from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
import json
# Create your views here.
from myapp.models import News, NewsCategory


class NewsCat(generics.GenericAPIView):
    def get(self, request):
        data = NewsCategory.objects.all()
        a = {
            "ok": True,
            "news_category": [i.json for i in data]
        }
        return JsonResponse(a, safe=False, json_dumps_params={'ensure_ascii': False})


news_category = NewsCat.as_view()


class AllNews(generics.GenericAPIView):

    def get(self, request):
        category = request.data
        try:
            if category['category_id']:
                pass
        except:
            return JsonResponse({'ok': False, 'error': 'pk is required'}, json_dumps_params={'ensure_ascii': False})
        news = News.objects.filter(news_category=category['category_id'])
        if news:
            a = {
                "ok": True,
                "news_category": NewsCategory.objects.get(pk=category["category_id"]).json,
                "news": [i.json for i in news]
            }
            return JsonResponse(a, safe=False, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"ok": False, "error": f"news is not found with category_id={category['category_id']}"}, safe=False, json_dumps_params={'ensure_ascii': False})


all_news = AllNews.as_view()


class OneNews(generics.GenericAPIView):
    def get(self, request):
        pk = request.data
        try:
            if pk['pk']:
                pass
        except:
            return JsonResponse({'ok': False, 'error': 'pk is required'}, json_dumps_params={'ensure_ascii': False})
        news = News.objects.filter(pk=pk['pk'])
        if news:
            a = {
                "ok": True,
                "news": news[0].json
            }
            return JsonResponse(a, safe=False, json_dumps_params={'ensure_ascii': False})
        return JsonResponse({"ok": False, "error": f"news is not found with pk={pk['pk']}"}, safe=False, json_dumps_params={'ensure_ascii': False})

one_news = OneNews.as_view()