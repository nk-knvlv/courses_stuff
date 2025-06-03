from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def hello_world(request):
    return JsonResponse({"key":"hello","value":"world"})