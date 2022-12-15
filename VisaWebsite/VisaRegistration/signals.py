from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Visa)
def create(created, sender, instance, **kwargs):
    if created:
        instance.valid_date = instance.date_issue + timezone.timedelta(days=int(instance.tariff_number.validity_period))
        instance.payment_amount = instance.tariff_number.validity_period * instance.tariff_number.coefficient
        instance.save()
