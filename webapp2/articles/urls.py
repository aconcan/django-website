from django.urls import path, include
from . import views

# Namespacing urls file
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    # Defining named capturing group and passing to article_detail as a parameter
    path('<slug:slug>/', views.article_detail, name='detail'),
]