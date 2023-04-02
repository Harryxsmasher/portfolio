from django.shortcuts import render
from django.http import HttpResponse
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Create your views here.

def home(request):
    context =  {'secureToken': env('SECURE_TOKEN'),'emailTo': env('EMAIL_TO'), 'emailFrom': env('EMAIL_FROM')}
    return render (request, 'base/index.html',  context)