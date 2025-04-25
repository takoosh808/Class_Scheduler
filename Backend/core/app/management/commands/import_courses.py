from django.core.management.base import BaseCommand
from app.models import Course
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Import courses from courses.xlsx into the Course model'

    def handle(self, *args, **kwargs):
        excel_path = os.path.join(os.getcwd(), 'app/api/courses.xlsx')

        if not os.path.exists(excel_path):
            self.stdout.write(self.style.ERROR(f"File not found: {excel_path}"))
            return

        df = pd.read_excel(excel_path)
        created = 0

        for _, row in df.iterrows():
            id_number = str(row['id_number']).strip()

            # Prevent duplicates
            if Course.objects.filter(id_number=id_number).exists():
                continue

            Course.objects.create(
                id_number=id_number,
                class_name=row['class_name'],
                Section_Number=row.get('Section_Number', 1),
                Instructor=row.get('Instructor', 'TBA'),
                Date=row.get('Date', ''),
                Time=row.get('Time', ''),
                Location=row.get('Location', ''),
                Enrollment=row.get('Enrollment', 0),
                Enrollment_max=row.get('Enrollment_max', 100),
                IsLab=row.get('IsLab', False)
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {created} new courses."))
