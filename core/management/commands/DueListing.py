from django.core.management.base import BaseCommand
from core.models import *

class Command(BaseCommand):
    def handle(self, **options):

        customer = User.objects.get(username="Jemoh")
        debtor = User.objects.get(username="Han")

        due_listing = DueListing(
        customer=customer,
        debtor=debtor,
        amount=30000000,
        debt_status='none'
        )
        due_listing.save()