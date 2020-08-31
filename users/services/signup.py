from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import Profile


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """Create user Profile if it doesn't exist and save"""
    if created:
        Profile.objects.create(user=instance)
    instance.objects.save()
   


