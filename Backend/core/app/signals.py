from django.db import connection
import os, logging

def load_initial_data(sender, **kwargs):
    logger = logging.getLogger(__name__)
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS(
                    SELECT FROM information_schema.tables
                    WHERE table_schema = 'public' AND table_name = 'courseapp'     
                );
            """)
            exists = cursor.fetchone()[0]
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sql_path = os.path.join(base_dir, 'app','api', 'Student.sql')
            with open(sql_path,'r') as file:
                sql = file.read()
            
            if not exists:
                logger.warning("Table 'courseapp' does not exist yet. Loading Students.sql")
                # cursor.execute(sql)
                return
            
            cursor.execute("SELECT COUNT(*) FROM courseapp;")
            row_count = cursor.fetchone()[0]
            if row_count == 0:
                logger.info("Loading Students.sql into empty courseapp table...")
                cursor.execute(sql)
                logger.info("Loaded students from Student.sql")
    except Exception as e:
        logger.warning(f"Error while loading Student.sql: {e}")