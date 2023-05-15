"""
<<<<<<< HEAD
ASGI config for Offensive_engine project.
=======
ASGI config for officensive_engine project.
>>>>>>> refs/remotes/origin/main

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Offensive_engine.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'officensive_engine.settings')
>>>>>>> refs/remotes/origin/main

application = get_asgi_application()
