from django.urls import path, re_path

from . import views

app_name = 'users'
urlpatterns = [
   path('',views.index, name='index'),
   path('<slug:link>/', views.profile, name='profile'),
   path('<slug:link>/settings/', views.settings, name='settings'),
]