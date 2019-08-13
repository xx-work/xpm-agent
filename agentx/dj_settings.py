import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'f&kcc4g^gj(+$945of9g%lm3g+t!#&2fxfo*$51mtrfn!p43_&'
INSTALLED_APPS = ['agentx.app']

MIDDLEWARE = []
TEMPLATES = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cso813',
        'USER': 'root',
        'PASSWORD': 'test@1q2w2e4R',
        'HOST': "192.168.2.227",
        'PORT': 33306,
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
