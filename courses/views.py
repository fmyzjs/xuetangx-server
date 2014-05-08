from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

def selected(request):
    email = request.POST['email']
    password = request.POST['password']

    courses_upcoming, courses_current, courses_past = xuetangx.courses_selected(email, password)

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses_upcoming,
        'courses.current': courses_current,
        'courses.past': courses_past,
    }))

def upcoming(request):
    email = request.POST['email']
    password = request.POST['password']

    courses = xuetangx.courses_upcoming(email, password)

    return HttpResponse(utils.template.respond({
        'courses.upcoming': courses,
    }))

def current(request):
    email = request.POST['email']
    password = request.POST['password']

    courses = xuetangx.courses_current(email, password)

    return HttpResponse(utils.template.respond({
        'courses.current': courses,
    }))

def past(request):
    email = request.POST['email']
    password = request.POST['password']

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
    query = request.POST.get('query', None)
    cid = request.POST.get('cid', None)
    started = __str2bool__(request.POST.get('started', 'false'))
    hasTA = __str2bool__(request.POST.get('hasTA', 'false'))

    result = xuetangx.courses_search(query, cid, started, hasTA)

    return HttpResponse(utils.template.respond({
        'courses.search': result,
    }))

def unenroll(request):
    url = request.POST.get('url')
    email = request.POST.get('email')
    password = request.POST.get('password')

    action = 'unenroll'

    success = xuetangx.courses_enrollment(email, password, url, action)

    return HttpResponse(utils.template.respond({
        'courses.unenroll': success,
    }))

def enroll(request):
    url = request.POST.get('url')
    email = request.POST.get('email')
    password = request.POST.get('password')

    action = 'enroll'

    success = xuetangx.courses_enrollment(email, password, url, action)

    return HttpResponse(utils.template.respond({
        'courses.enroll': success,
    }))

def lectures(request):
    email = request.POST['email']
    password = request.POST['password']
    url = request.POST['url']

    lectures = xuetangx.courses_lectures(email, password, url)

    return HttpResponse(utils.template.respond({
        'courses.lectures': lectures,
    }))

def lecture(request):
    email = request.POST['email']
    password = request.POST['password']
    url = request.POST['url']

    items = xuetangx.courses_lecture(email, password, url)

    return HttpResponse(utils.template.respond({
        'courses.lecture': items,
    }))

def ware(request):
    email = request.POST['email']
    password = request.POST['password']
    url = request.POST['url']

    chapters = xuetangx.courses_ware(email, password, url)

    return HttpResponse(utils.template.respond({
        'courses.ware': chapters,
    }))

