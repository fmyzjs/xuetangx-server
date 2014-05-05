from django.shortcuts import render

from django.http import HttpResponse

def verify(request):
    return HttpResponse("You're at the student verify.")

def info(request):
    return HttpResponse("You're at the student info.")
