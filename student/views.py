from django.http import HttpResponse

import client.xuetangx as xuetangx
import utils.template

def verify(request):
    email = request.POST['email']
    password = request.POST['password']

    valid = xuetangx.verify(email, password)

    return HttpResponse(utils.template.respond({'student.verify': valid}))

def info(request):
    email = request.POST['email']
    password = request.POST['password']

    name, nickname = xuetangx.student_info(email, password)

    return HttpResponse(utils.template.respond({
        'student.name': name,
        'student.nickname': nickname}))
