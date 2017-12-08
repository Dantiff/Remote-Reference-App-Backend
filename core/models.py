from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, blank=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'tbl_profiles'

    def __str__(self):
        return self.acc_name


class DueListing(models.Model):

    DEBT_CHOICES = (
        ('full', 'Fully Paid'),
        ('partial', 'Partially Paid'),
        ('none', 'Not Paid'),
    )
    customer = models.OneToOneField(User, related_name='due_listing_customer', on_delete=models.CASCADE)
    debtor = models.OneToOneField(User, related_name='due_listing_debtor', on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, blank=True)
    debt_status = models.CharField(max_length=50, default='none', choices=DEBT_CHOICES)

    class Meta:
        db_table = 'tbl_due_listing'
        ordering = ('amount',)


    def __str__(self):
        return self.customer
