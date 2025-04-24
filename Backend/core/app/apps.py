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
        # logger = logging.getLogger(__name__)
        # try:
        #     with connection.cursor() as cursor:
        #         cursor.execute('SELECT COUNT(*) FROM courseapp;')
        #         row_count = cursor.fetchone()[0]

        #         if row_count == 0:
        #             logger.info("Student table is empty. Loading Students.sql...")

        #             base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #             sql_path = os.path.join(base_dir,'api','Students.sql')

        #             with open(sql_path,'r') as file:
        #                 sql = file.read()
        #             cursor.execute(sql)
        #             logger.info("Successfully loaded Students.sql!")
        #         else:
        #             logger.info("Student table already populated, Skipping sql load")
        # except (OperationalError,ProgrammingError) as e:
        #     logger.warning(f"Startup data load skipped: {e}")