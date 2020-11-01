from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=get_user_model())
def post_save_create_profile(sender, instance, created, **kwargs):
    print(sender, instance, created, kwargs)
    if created:
        Profile.objects.create(user=instance)