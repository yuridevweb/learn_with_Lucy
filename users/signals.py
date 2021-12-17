from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from main.models import Pet, Dwelling, Avatar


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance)
        # , profile_pet=Pet.objects.get(name="pet_0"),
        # profile_avatar=Avatar.objects.get(name="avatar_0"),
        # profile_dwelling=Dwelling.objects.get(name="dwelling_0"))


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
