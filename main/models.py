from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='pet_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Dwelling(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='dwelling_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='avatar_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def obtain_choice(choice):
        if choice.startswith('ava'):
            return Avatar.objects.get(name=choice)
        elif choice.startswith('pet'):
            return Pet.objects.get(name=choice)
        else:
            return Dwelling.objects.get(name=choice)
