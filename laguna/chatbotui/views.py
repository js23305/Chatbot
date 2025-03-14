from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def chatbotui(request):

    template = loader.get_template('chat.html')

    context = {
        'title': 'Chatbot',
        'content': 'Welcome to the chatbot'
    }

    return HttpResponse(template.render(context, request))
    

def send_film_to_user(data):
    print("Hello there")

    return JsonResponse({
        "message": "Sleepy Hollow",
        "status_code": 200
    })
    

