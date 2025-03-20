from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import requests

def login(request):

    template = loader.get_template('login.html')

    context = {
        'title': 'Login',
        'content': 'Welcome to the login page'
    }

    return HttpResponse(template.render(context, request))