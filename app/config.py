from email import charset
import os
import string, random


class DevConfig(object):
    SECRET_KEY = '/*(Rhg84/651|]+*/[8a-+GHas8654]'
    ENV = 'development'
    DEBUG = True


chars = ''.join(
    [string.ascii_letters, string.digits, string.punctuation]
    ).replace('\'', '').replace('"', '').replace('\\', '')

class ProductionConfig(object):

    SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for _ in range(100)])
    ENV = 'production'
    DEBUG = False