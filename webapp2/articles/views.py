from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

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
    if request.method == 'POST':
        # Validating the data we receive on the request.POST object against our model
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # Not committing to DB. Returning instance so we can set the author to be current user 
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    # Creating instance of form to output to article_create.html
    form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })