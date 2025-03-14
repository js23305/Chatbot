from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

def chatbotui(request):

    template = loader.get_template('chat.html')

    context = {
        'title': 'Chatbot',
        'content': 'Welcome to the chatbot'
    }

    return HttpResponse(template.render(context, request))
    