# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, User

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    card_number = models.CharField(max_length=16, unique=True, blank=True)
    cvv_number = models.CharField(max_length=3, blank=True)
    exp_date = models.DateField(blank=True, null=True)