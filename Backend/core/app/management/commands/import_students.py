from django.core.management.base import BaseCommand
from app.models import Student
import csv
import os

class Command(BaseCommand):
    help = 'Import students from students.csv'

    def handle(self, *args, **kwargs):
        filepath = os.path.join(os.getcwd(), 'app/api/students.csv')

        if not os.path.exists(filepath):
            self.stdout.write(self.style.ERROR("students.csv not found"))
            return

        created_count = 0

        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id_number = row['id_number'].strip()

                if not Student.objects.filter(id_number=id_number).exists():
                    Student.objects.create(
                        id_number=id_number,
                        first_name=row['first_name'].strip(),
                        last_name=row['last_name'].strip(),
                        password=row['password'].strip()
                    )
                    created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {created_count} students"))