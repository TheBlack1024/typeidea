from .base import * #NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test1',
        'USER': "root",
        'PASSWORD': "mysql123",
        'HOST': "127.0.0.1",
        'PORT': 3306,
    }
}