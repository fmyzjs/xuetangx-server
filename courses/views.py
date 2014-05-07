from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

def selected(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    try:
        courses_upcoming, courses_current, courses_past = xuetangx.courses_selected(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses_upcoming,
        'courses.current': courses_current,
        'courses.past': courses_past,
    }))

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

    try:
        courses = xuetangx.courses_current(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({
        'courses.current': courses,
    }))

def past(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    try:
        courses = xuetangx.courses_past(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({
        'courses.past': courses,
    }))

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

