# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .utils import generate_card_info

@receiver(post_save, sender=CustomUser)
def assign_card_info(sender, instance, created, **kwargs):
    if created:
        # Generate unique card info
        card_info = generate_card_info()
        instance.card_number = card_info['card_number']
        instance.cvv_number = card_info['cvv_number']
        instance.exp_date = card_info['exp_date']
        instance.save()