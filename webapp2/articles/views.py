from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    # Querying DB for article matching slug argument and passing to article_detail template for rendering
    article = Article.objects.get(slug=slug) 
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    return render(request, 'articles/article_create.html')