import urllib

from client.csrfopner import CSRFOpenerDirector
import utils.admin

HTTP = 'http://'
HTTPS = 'https://'
HOST = 'www.xuetangx.com'
LOGIN_PAGE = HTTPS + HOST + '/login'
LOGIN_URL = HTTPS + HOST + '/login_ajax'
DASHBOARD = HTTPS + HOST + '/dashboard'

class AutoEmailOpener:
    import socket
    def __init__(self, opener):
        self.__opener__ = opener
    def __unicode__(self):
        return self.__opener__.__str__()
    def open(self, fullurl, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        try:
            return self.__opener__.open(fullurl, data, timeout)
        except Exception as e:
            utils.admin.email_http_error(e, self.__opener__, fullurl, data)
            raise e

class AuthenticationError(Exception):
    pass

def __get_opener__(email, password):
    """
    email: str
    password: str
    => CSRFOpenerDirector
    """
    opener = AutoEmailOpener(CSRFOpenerDirector())
    opener.open(LOGIN_PAGE)
    postdata = urllib.urlencode({
        'email': email,
        'password': password}).encode('utf-8')
    resp = opener.open(LOGIN_URL, postdata).read()

    import json
    try:
        success = json.loads(resp)['success']
    except (ValueError, KeyError) as e:
        utils.admin.email_json_error(e, resp)
        raise e

    if not success:
        raise AuthenticationError()

    return opener

def verify(email, password):
    """
    email: str
    password: str
    => bool. May raise Exception.
    """
    opener = __get_opener__(email, password)
    return (True if opener else False)

def student_info(email, password):
    """
    email: str
    password: str
    => (name, nickname)
    """
    opener = __get_opener__(email, password)
    page = opener.open(DASHBOARD).read()
    from BeautifulSoup import BeautifulSoup
    try:
        parsed_page = BeautifulSoup(page)
        name = parsed_page.body.find('span', attrs={'class': 'data'}).text
        nickname = parsed_page.body.find('h1', attrs={'class': 'user-name'}).text
    except Exception as e:
        utils.admin.email_html_error(e, page)
        raise e

    return (name, nickname)
