from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64


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


class Breed(models.Model):

    name = models.CharField(max_length=100, blank=False)
    size = models.CharField(max_length=50, blank=False)
    friendliness = models.IntegerField(blank=False)
    trainability = models.IntegerField(blank=False)
    shreddingamount = models.IntegerField(blank=False)
    exerciseneeds = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.name)


class Dog(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed)
    gender = models.CharField(max_length=10, blank=False)
    color = models.CharField(max_length=50, blank=False)
    favoritefood = models.CharField(max_length=100, blank=False)
    favoritetoy = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)
