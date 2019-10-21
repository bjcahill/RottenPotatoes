from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/details/<slug:id>/', views.details, name='details')
]
