from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(default='dog.svg', upload_to='pet_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Dwelling(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(default='house.svg', upload_to='dwelling_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Avatar(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(default='house.svg', upload_to='avatar_pics')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
