from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('news/<int:id>/', views.news, name='news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)