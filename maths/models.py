from django.db import models
import math
from django.contrib.auth.models import User

# Create your models here.


class MathHighScore(models.Model):

    id = models.AutoField(primary_key=True)
    score = models.IntegerField(default='0')
    time = models.IntegerField(default='0')
    formated_time = models.CharField(max_length=30, default='0')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.username

    def format_time(self):
        hours = math.floor(self.time / 3600000)
        remainder = self.time - (hours * 3600000)
        if hours < 10:
            hours = "0" + str(hours)

        minutes = math.floor(remainder / 60000)
        remainder -= (minutes * 60000)
        if minutes < 10:
            minutes = "0" + str(minutes)

        seconds = math.floor(remainder / 1000)
        remainder -= (seconds * 1000)
        if seconds < 10:
            seconds = "0" + str(seconds)

        self.formated_time = str(hours) + ":" + \
            str(minutes) + ":" + str(seconds)
        self.save()

    def check_high_score(self, new_score, elapsedTime):
        if self.score < new_score:
            self.score = new_score
            self.time = elapsedTime
        elif self.score == new_score:
            if self.time > elapsedTime:
                self.time = elapsedTime
        self.save()

    class Meta:
        ordering = ('-score', 'time')


class SimpleMathScore(MathHighScore):
    pass


class AdvMathScore(models.Model):

    id = models.AutoField(primary_key=True)
    score = models.IntegerField(default='0')
    time = models.IntegerField(default='0')
    formated_time = models.CharField(max_length=30, default='0')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.username

    def format_time(self):
        hours = math.floor(self.time / 3600000)
        remainder = self.time - (hours * 3600000)
        if hours < 10:
            hours = "0" + str(hours)

        minutes = math.floor(remainder / 60000)
        remainder -= (minutes * 60000)
        if minutes < 10:
            minutes = "0" + str(minutes)

        seconds = math.floor(remainder / 1000)
        remainder -= (seconds * 1000)
        if seconds < 10:
            seconds = "0" + str(seconds)

        self.formated_time = str(hours) + ":" + \
            str(minutes) + ":" + str(seconds)
        self.save()

    def check_high_score(self, new_score, elapsedTime):
        if self.score < new_score:
            self.score = new_score
            self.time = elapsedTime
        elif self.score == new_score:
            if self.time > elapsedTime:
                self.time = elapsedTime
        self.save()

    class Meta:
        ordering = ('-score', 'time')
