from django.apps import AppConfig
from django.db.utils import OperationalError,ProgrammingError
from django.db import connection
from django.conf import settings
import os, logging


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        import app.signals