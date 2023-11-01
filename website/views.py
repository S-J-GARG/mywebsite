from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    first=User.objects.get(id=1)
    return HttpResponse(first)