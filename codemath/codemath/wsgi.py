import os
import sys

path = '/home/codemath/my-first-blog'  # aquí utiliza tu propio usuario, sin los simbolos < y >
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'codemath.codemath.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
