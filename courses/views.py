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

def categories(request):
    return HttpResponse(utils.template.respond({
        'courses.categories': xuetangx.courses_categories(),
    }))

def __str2bool__(string):
    return string.lower() in ('yes', 'true', 't', '1')

def search(request):
    query = request.GET.get('query', None)
    cid = request.GET.get('cid', None)
    started = __str2bool__(request.GET.get('started', 'false'))
    hasTA = __str2bool__(request.GET.get('hasTA', 'false'))

    result = xuetangx.courses_search(query, cid, started, hasTA)

    return HttpResponse(utils.template.respond({
        'courses.search': result,
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

