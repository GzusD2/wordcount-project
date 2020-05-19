from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('bacon', views.bacon),
    path('count', views.count, name='count'),
    path('about', views.about, name='about'),
]
