from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from art import *


@csrf_exempt
def index(request):

    text = request.POST.get("text")

    return HttpResponse(f"{text2art('{text}', font='black')}")
