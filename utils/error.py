from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

import client.xuetangx as xuetangx
import utils.template

class AuthenFailMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, xuetangx.AuthenticationError):
            return HttpResponse(utils.template.authen_error())
        elif isinstance(exception, MultiValueDictKeyError):
            return HttpResponse(utils.template.invalid_request())
        else:
            raise exception
