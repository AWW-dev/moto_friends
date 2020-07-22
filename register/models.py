from django.db import models
from django.contrib.auth.models import User
# Create your models here.

BIKE = (
    (1, "Chopper/cruiser"),
    (2, "Cross/Enduro"),
    (3, "ATV"),
    (4, "Szosa/turystyk"),
)

WOJE = (
    (1, "DOLNOŚLĄSKIE"),
    (2, "KUJAWSKO-POMORSKIE"),
    (3, "LUBELSKIE"),
    (4, "LUBUSKIE"),
    (5, "ŁÓDZKIE"),
    (6, "MAŁOPOLSKIE"),
    (7, "MAZOWIECKIE"),
    (8, "OPOLSKIE"),
    (9, "PODKARPACKIE"),
    (10, "PODLASKIE"),
    (11, "POMORSKIE"),
    (12, "ŚLĄSKIE"),
    (13, "ŚWIĘTOKRZYSKIE"),
    (14, "WARMIŃSKO-MAZURSKIE"),
    (15, "WIELKOPOLSKIE"),
    (16, "ZACHODNIOPOMORSKIE"),
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.IntegerField(choices=WOJE, verbose_name="skąd ruszasz?")
    age = models.IntegerField(verbose_name="Twój wiek?")
    bike_type = models.IntegerField(choices=BIKE, verbose_name="typ motocykla")
    about = models.TextField(verbose_name="Powiedz coś o sobie!")