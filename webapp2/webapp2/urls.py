from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.homepage),
    # Including the urls file from the articles app
    path('articles/', include('articles.urls')),
]

# Appending method to urlpatterns so Django knows how to serve up static files
urlpatterns += staticfiles_urlpatterns()