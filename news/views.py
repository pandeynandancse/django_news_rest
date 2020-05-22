from django.shortcuts import render

# Create your views here.
import requests
from django.http.response import HttpResponse
from rest_framework import viewsets
from news.models import News
from news.newsserializer import NewsSerializer

from rest_framework.decorators import api_view
# no. of rows






def index():
    json_obj = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=992d09763cc4473d8612788b6ddc1326').json()

    articles = json_obj['articles']
    print(type(articles))
    News.objects.all().delete()
    for i, article in enumerate(articles):

        source= article['source']['name']
        title= article['title']
        description = article['description']
        url = article['url']
        urlToImage= article['urlToImage'] 
        newsinfo = News(source = source,title=title,description =description,url=url)
        data = {"source":source,"title":title,"description":description,"url":url,"urlToImage":urlToImage}
        newsinfo.save()
    print("done")
    return 







class NewsViewSet(viewsets.ModelViewSet):
	queryset  = News.objects.all()
	print(1)
	index()
	serializer_class  = NewsSerializer





