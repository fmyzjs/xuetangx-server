from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

def selected(request):
    email = request.GET['email']
    password = request.GET['password']

    courses_upcoming, courses_current, courses_past = xuetangx.courses_selected(email, password)

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses_upcoming,
        'courses.current': courses_current,
        'courses.past': courses_past,
    }))

def upcoming(request):
    email = request.GET['email']
    password = request.GET['password']

    courses = xuetangx.courses_upcoming(email, password)

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses,
    }))

def current(request):
    email = request.GET['email']
    password = request.GET['password']

    courses = xuetangx.courses_current(email, password)

    return HttpResponse(utils.template.respond({
        'courses.current': courses,
    }))

def past(request):
    email = request.GET['email']
    password = request.GET['password']

    courses = xuetangx.courses_past(email, password)

    return HttpResponse(utils.template.respond({
        'courses.past': courses,
    }))

def search(request):
    key = request.GET['key']
    category = request.GET['category']
    started = bool(request.GET['started'])
    hasTA = bool(request.GET['hasTA'])
    # TODO: check whether category in the list

    return HttpResponse(utils.template.respond({
        'TODO': 'TODO',
    }))

def about(request):
    url = request.GET['url']

    return HttpResponse("You're at the courses about.")

def info(request):
    email = request.GET['email']
    password = request.GET['password']
    url = request.GET['url']

    return HttpResponse("You're at the courses info.")

def ware(request):
    email = request.GET['email']
    password = request.GET['password']
    url = request.GET['url']

    return HttpResponse("You're at the courses ware.")

