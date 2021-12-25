import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system("python3 manage.py ap_filler")
        # os.system("python3 manage.py as_filler")
        # os.system("python3 manage.py asc_filler")
        # os.system("python3 manage.py cl_filler")
        # os.system("python3 manage.py hw_filler")
        # os.system("python3 manage.py lh_filler")
        # os.system("python3 manage.py st_filler")
        # os.system("python3 manage.py tc_filler")
        # os.system("python3 manage.py tt_filler")
