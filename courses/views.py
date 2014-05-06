from django.shortcuts import render

from django.http import HttpResponse

def selected(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses selected.")

def upcoming(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses upcoming.")

def current(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses current.")

def past(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses past.")

def search(request):
    try:
        key = request.GET['key']
        category = request.GET['category']
        started = request.GET['started'] # bool
        hasTA = request.GET['hasTA'] # bool
        # TODO: check whether category in the list
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses search.")

def about(request):
    try:
        url = request.GET['url']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses about.")

def info(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
        url = request.GET['url']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses info.")

def ware(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
        url = request.GET['url']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    return HttpResponse("You're at the courses ware.")

