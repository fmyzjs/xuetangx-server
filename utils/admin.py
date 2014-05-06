from django.core.mail import send_mail

def email_notice(subject, message):
    send_mail(subject,
        message,
        'xuetangx.leonhuang@gmail.com',
        ['leonxinhuang+xuetangx@gmail.com'],
        fail_silently=True)

def email_http_error(exception, opener, url, data=None):
    email_notice(
        '[XuetangX] HTTP(S) Error',
        """Exception: %s
Opener: %s
URL: %s
Data: %s
""" % (opener, url, data, exception))

def email_json_error(exception, string):
    email_notice(
        '[XuetangX] JSON Parse Error',
        """Exception: %s
String: %s
""" % (string, exception))

def email_html_error(exception, page):
    email_notice(
        '[XuetangX] HTML Parse Error',
        """Exception: %s
Page: %s
""" % (page, exception))
