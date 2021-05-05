from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from art import *

def index(request):
    return HttpResponse(f"{tprint('Victor', font='cola')}")
