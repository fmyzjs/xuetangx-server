HTTP = "http://"
HTTPS = "https://"
HOST = "www.xuetangx.com"
LOGIN_PAGE = HTTPS + HOST + "/login"
LOGIN_URL = HTTPS + HOST + "/login_ajax"

import urllib
from client.csrfopner import CSRFOpenerDirector

def verify(email, password):
    """
    email: str
    password: str
    => bool. May raise Exception.
    """
    opener = CSRFOpenerDirector()

    opener.open(LOGIN_PAGE)

    postdata = urllib.urlencode({
        'email': email,
        'password': password}).encode('utf-8')

    resp = opener.open(LOGIN_URL, postdata).read()

    import json
    return json.loads(resp)['success']
