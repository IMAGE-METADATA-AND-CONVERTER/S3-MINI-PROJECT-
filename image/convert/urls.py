from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="index"),
    path('index/', views.index,name="index"),
    path('meta part/', views.getmetadata,name="meta part"),
     path('converter/', views.convert,name="converter"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
