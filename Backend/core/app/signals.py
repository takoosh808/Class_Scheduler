from django.db import connection
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os, logging


def table_exists(table_name):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT EXISTS(
                SELECT FROM information_schema.tables
                WHERE table_name = %s
            );
        """,[table_name])
        return cursor.fetchone()[0]


@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    logger = logging.getLogger(__name__)
    # logger.info(f"Signal fired for sender: {sender.name}")

    if sender.label != 'app':
        return
    
    try:
        if table_exists('student'):
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM student;")
                count = cursor.fetchone()[0]
                if count >0:
                    logger.info("Student table already populated, Truncating and reloading")
                    cursor.execute("TRUNCATE TABLE student RESTART IDENTITY CASCADE;")
                else:
                    logger.info("Student table is empty, loading initial data...")

                base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                sql_path = os.path.join(base_dir, 'app','api', 'Student.sql')
                with open(sql_path,'r') as file:
                    sql = file.read()
                    cursor.execute(sql)
        else:
            logger.warning("Student table is not created, please create and retry...")
            
    except Exception as e:
        logger.warning(f"Error while loading Student.sql: {e}")