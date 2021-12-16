from django.db import models
from django.contrib.auth.models import User
from main.models import Pet, Dwelling, Avatar
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0, null=True)
    coins = models.IntegerField(default=10, null=True)
    profile_avatar = models.ForeignKey(
        Avatar, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, null=True)
    profile_dwelling = models.ForeignKey(
        Dwelling, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def coins_earned(self, score):
        earned_coins = score / 5
        self.coins += earned_coins
        self.save()
        return "Thanks for playing! You earned %s coins!" % int(earned_coins)

    def purschase(self, item):
        if self.coins < item.price:
            return "Sorry, not  enough coins!"
        else:
            self.coins -= item.price
            if item.name.startswith('ava'):
                self.profile_avatar = item
            elif item.name.startswith('pet'):
                self.profile_pet = item
            else:
                self.profile_dwelling = item
        self.save()
        return "Congratulations! Your profile has been updated!"
