from django.apps import AppConfig
from django.db.utils import OperationalError,ProgrammingError
from django.db import connection
from django.conf import settings
from django.db.models.signals import post_migrate
import os, logging


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .signals import load_initial_data
        post_migrate.connect(load_initial_data, sender=self)