from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template
import utils.admin

def verify(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
    except (ValueError, KeyError) as e:
        return HttpResponse(utils.template.invalid_request())

    try:
        valid = xuetangx.verify(email, password)
    except Exception as e:
        utils.admin.email_notice(request.POST, e)
        return HttpResponse(utils.template.server_error())

    return HttpResponse(utils.template.respond({'student.verify': valid}))

def info(request):
    return HttpResponse("You're at the student info.")
