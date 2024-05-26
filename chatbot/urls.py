from django.urls import path
from chatbot import views 

urlpatterns = [
    path('', views.start),
    path('chatbot', views.chatbot, name='chatbot'),
    path('stats', views.stats, name='stats')
]


