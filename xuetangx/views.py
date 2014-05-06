from django.http import HttpResponse

import utils.template

def my_custom_404_view(request):
    return HttpResponse(utils.template.invalid_request())

def my_custom_error_view(request):
    return HttpResponse(utils.template.server_error())
