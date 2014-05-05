class CSRFOpenerDirector:
    import socket
    def __init__(self):
        import cookielib
        import urllib2
        self.__cookie__ = cookielib.CookieJar()
        cjhdr = urllib2.HTTPCookieProcessor(self.__cookie__)
        self.__opener__ = urllib2.build_opener(cjhdr)
    def open(self, fullurl, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        csrftoken = None
        for cookie in self.__cookie__:
            if cookie.name == 'csrftoken':
                csrftoken = cookie.value
        if csrftoken:
            self.__opener__.addheaders.append(("X-CSRFToken", csrftoken))
        return self.__opener__.open(fullurl, data, timeout)
