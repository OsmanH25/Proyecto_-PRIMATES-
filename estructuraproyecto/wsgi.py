"""
WSGI config for estructuraproyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estructuraproyecto.settings') #aca se configura el wsgi que se va a usar para el proyecto cpn la ruta de la carpeta settings

application = get_wsgi_application()


# este archivo hace referencia al wsgi que se va a usar para el proyecto, en este caso se usa el wsgi de la carpeta settings