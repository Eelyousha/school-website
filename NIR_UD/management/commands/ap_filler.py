from random import choice

from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime

from NIR_UD.models import *

fake = Faker()


class Command(BaseCommand):
    def answers(self, cnt):
        students_ids = list(
            Students.objects.values_list('id', flat=True))

        classes_ids = list(
            Classes.objects.values_list('id', flat=True))

        subject_ids = list(
            AcademicSubjects.objects.values_list('id', flat=True))
        print(students_ids)
        print(classes_ids)
        print(subject_ids)

        answers = []
        for _ in range(cnt):
            subject_id = choice(subject_ids)
            students_id = choice(students_ids)
            classes_id = choice(classes_ids)
            answers.append(AcademicPerformance(
                lesson_date=fake.date_between_dates(date_start=datetime(2019, 1, 1)),
                is_appeared=fake.pybool(),
                student_id_id=students_id,
                class_id_id=classes_id,
                subject_id_id=subject_id,
                student_mark=fake.random_int(min=2, max=5)
            ))
        AcademicPerformance.objects.bulk_create(answers)

    def handle(self, *args, **options):
        size = [20, 10001, 100001, 1000001]
        self.answers(size[0])
