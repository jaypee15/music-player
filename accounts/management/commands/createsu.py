import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username="username").exists():
            User.objects.create_superuser(
                username=os.getenv("username"),
                password=os.getenv("password")
            )
        print('Superuser has been created.')
        