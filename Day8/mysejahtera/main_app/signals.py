from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import HealthInfo, Vaccine


@receiver(post_save, sender = User)
def create_health(sender, instance , created, **kwargs):
    if created:
        HealthInfo.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_health(sender, instance , **kwargs):
    instance.healthinfo.save()

@receiver(post_save, sender = User)
def save_vaccine(sender, instance, created , **kwargs):
    if created:
        Vaccine.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_vaccine(sender, instance , **kwargs):
    instance.vaccine.save()