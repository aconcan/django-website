from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('work/', views.work, name='work'),
    path('', views.homepage, name='home'),
    # Including the urls file from the articles app
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

# Appending method to urlpatterns so Django knows how to serve up static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)