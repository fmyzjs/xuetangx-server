#!/usr/bin/env python
# encoding: utf-8

import json

__VALID__ = 'valid'
__ERROR__ = 'error'
__AUTHEN__ = 'authen'

def invalid_request():
    return json.dumps({
        __VALID__: False,
    })

def server_error():
    return json.dumps({
        __VALID__: True,
        __ERROR__: True,
    })

def authen_error():
    return json.dumps({
        __VALID__: True,
        __ERROR__: False,
        __AUTHEN__: False,
    })

__DEFAULT_OK__ = {
    __VALID__: True,
    __ERROR__: False,
    __AUTHEN__: True,
}

def respond(content):
    assert isinstance(content, dict)
    for k, v in __DEFAULT_OK__.items():
        assert k not in content
        content[k] = v
    return json.dumps(content)
