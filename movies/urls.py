from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<slug:link>/', views.details, name='details'),
    path('submitMovie/', views.submitMovie, name='submitMovie'),
    path('submitReview/', views.submitReview, name='submitReview'),
    path('search/', views.search, name='search'),
    path('nowplaying/', views.nowplaying, name = 'nowplaying'),
]
