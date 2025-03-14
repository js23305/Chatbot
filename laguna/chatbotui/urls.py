from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbotui, name='chatbotui'),
]