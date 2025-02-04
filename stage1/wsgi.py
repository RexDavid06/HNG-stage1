"""
WSGI config for stage1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from waitress import serve
from stage1.wsgi import application

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stage1.settings")
    serve(application, host="0.0.0.0", port=8000)

