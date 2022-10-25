from __future__ import unicode_literals
from unicodedata import name

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

# from numpy import size


class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)


class EventAdmin(admin.ModelAdmin):
    list_display = ("eventtype", "timestamp")


class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ("owner", "key")


# Create your models here.
class Breed(models.Model):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

    SIZE = (
        (TINY, "Tiny"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    )
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=6, choices=SIZE, default=SMALL)
    friendliness = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    sheddingamount = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exerciseneeds = models.IntegerField(
        default=3, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    favoritefood = models.CharField(max_length=75)
    favoritetoy = models.CharField(max_length=75)
