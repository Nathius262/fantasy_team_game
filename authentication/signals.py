from django.dispatch import receiver
from django.db.models.signals import post_save
from user.models import Profile
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def createUserProfile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)