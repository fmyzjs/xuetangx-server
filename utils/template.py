import json

__VALID__ = 'valid'
__ERROR__ = 'error'

def invalid_request():
    return json.dumps({
        __VALID__: False,
    })

def server_error():
    return json.dumps({
        __VALID__: True,
        __ERROR__: True,
    })

__DEFAULT_OK__ = {
    __VALID__: True,
    __ERROR__: False,
}

def respond(content):
    assert isinstance(content, dict)
    for k, v in __DEFAULT_OK__.items():
        assert k not in content
        content[k] = v
    return json.dumps(content)
