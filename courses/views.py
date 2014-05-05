from django.shortcuts import render

from django.http import HttpResponse

def verify(request):
    return HttpResponse("You're at the student verify.")

def info(request):
    return HttpResponse("You're at the student info.")

def selected(request):
    return HttpResponse("You're at the courses selected.")

def upcoming(request):
    return HttpResponse("You're at the courses upcoming.")

def current(request):
    return HttpResponse("You're at the courses current.")

def past(request):
    return HttpResponse("You're at the courses past.")

def search(request):
    return HttpResponse("You're at the courses search.")

def about(request):
    return HttpResponse("You're at the courses about.")

def info(request):
    return HttpResponse("You're at the courses info.")

def ware(request):
    return HttpResponse("You're at the courses ware.")

