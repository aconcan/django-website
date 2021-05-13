from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list),
    # Defining named capturing group and passing to article_detail as a parameter 
    path('<slug:slug>/', views.article_detail),
]