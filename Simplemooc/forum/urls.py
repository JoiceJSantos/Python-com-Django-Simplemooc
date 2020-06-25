from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
   path('', views.index, name='index'),
   path('tag/<tag>/', views.index, name='index_tagged'),
   path('respostas/<pk>/correta/', views.reply_correct, name='reply_correct'),
   path('respostas/<pk>/incorreta/', views.reply_incorrect, name='reply_incorrect'),
   path('<slug>/', views.thread, name='thread'),

]