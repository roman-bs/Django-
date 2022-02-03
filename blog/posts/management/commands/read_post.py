import logging

import csv

from django.conf import settings


from django.core.management.base import BaseCommand
from posts.models import Post

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Print posts"

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / "posts.csv", "r") as file:
            reader = csv.reader(file)
            for row
                writer.writerow([post.id, post.title])