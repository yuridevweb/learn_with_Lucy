from django.db import models
from django.contrib.auth.models import User
from main.models import Pet, Dwelling
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)
    image = models.FileField(default='default.svg')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, null=True)
    profile_dwelling = models.ForeignKey(
        Dwelling, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def pet_purschase(self, pet):
        if self.coins < pet.price:
            return "Sorry, not  enough coins!"
        else:
            self.coins -= pet.price
            self.profile_pet = pet
            self.save()
            return "Congratulations! You have a new pet!"
