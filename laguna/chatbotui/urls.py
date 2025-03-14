from django.urls import path
from chatbotui.views import chatbotui, send_film_to_user

urlpatterns = [
    path('', chatbotui, name='chatbotui'),
    path('send_film_to_user/', send_film_to_user),
]