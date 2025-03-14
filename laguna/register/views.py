from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def register(request):

    template = loader.get_template('register.html')

    context = {
        'title': 'register',
        'content': 'Welcome to the register page'
    }

    return HttpResponse(template.render(context, request))