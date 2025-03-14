from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests

def register(request):

    template = loader.get_template('register.html')

    context = {
        'title': 'register',
        'content': 'Welcome to the register page'
    }

    return HttpResponse(template.render(context, request))


def register_user_with_firebase(data):

    print("Hello there this is the register user method")

    URL = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDUawoWlHYX5u80ikPzS9nRfZ_vhaSK2EQ"

    jsondata = {
        "email": "test@test.com",
        "password": "test123",
        "returnSecureToken": True
    }

    response = requests.post(URL, json=jsondata, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        return JsonResponse({
            "message": response.json(),
            "status_code": 200
        })
    
    else:
        return JsonResponse({
            "message": response.json(),
            "status_code": 400
        })