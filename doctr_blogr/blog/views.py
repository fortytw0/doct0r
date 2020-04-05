from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article , Tag

# Create your views here.


def index(request) : 

    all_articles = Article.objects.all()[:15]
    all_tags = Tag.objects.all()

    context_dict = {"all_articles":all_articles,"all_tags":all_tags}

    return render(request , "blog/base.html" , context=context_dict)

def article_view(request) : 

    return(HttpResponse("<h1>To dO</h1>"))