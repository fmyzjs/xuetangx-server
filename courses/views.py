from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

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

    try:
        courses = xuetangx.courses_upcoming(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses,
    }))

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

