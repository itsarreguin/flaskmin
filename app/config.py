import string, random


CHARS = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

GENERATE_STRING = ''.join([random.SystemRandom().choice(CHARS) for _ in range(100)])


class DevConfig(object):
    ENV = 'development'
    SECRET_KEY = '/*(Rhg84/651|]+*/[8a-+GHas8654]'
    DEBUG = True


class ProductionConfig(object):
    ENV = 'production'
    SECRET_KEY = GENERATE_STRING
    DEBUG = False