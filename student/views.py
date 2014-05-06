from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

def verify(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    try:
        valid = xuetangx.verify(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({'student.verify': valid}))

def info(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
    except (ValueError, KeyError):
        return HttpResponse(utils.template.invalid_request())

    try:
        name, nickname = xuetangx.student_info(email, password)
    except xuetangx.AuthenticationError:
        return HttpResponse(utils.template.authen_error())
    except Exception:
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({
        'student.name': name,
        'student.nickname': nickname}))
