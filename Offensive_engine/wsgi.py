"""
<<<<<<< HEAD
WSGI config for Offensive_engine project.
=======
WSGI config for officensive_engine project.
>>>>>>> refs/remotes/origin/main

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Offensive_engine.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'officensive_engine.settings')
>>>>>>> refs/remotes/origin/main

application = get_wsgi_application()
