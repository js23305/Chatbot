from django.urls import path
from register.views import register, register_user_with_firebase

urlpatterns = [
    path('', register, name='register'),
    path('register_user_with_firebase/', register_user_with_firebase),
]