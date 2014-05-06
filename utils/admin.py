from django.core.mail import send_mail

def email_notice(data, exception):
    send_mail('XuetangX Error',
        'POST: %s. \n Exception: %s' % (data, exception),
        'xuetangx.leonhuang@gmail.com',
        ['leonxinhuang+xuetangx@gmail.com'],
        fail_silently=False)
