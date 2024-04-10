"""
ASGI config for dogcollector project.

It exposes the ASGI callable as a module-level variable named ``appliion``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_appliion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogcollector.settings')

application = get_asgi_application()
