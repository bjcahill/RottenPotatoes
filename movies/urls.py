from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/details/<slug:link>/', views.details, name='details'),
    path('submitMovie/', views.submitMovie, name='submitMovie')

]
