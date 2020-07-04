from django.contrib.auth.models import User
from django.db import models

# Create your models here.
STYLE = (
    (1, "POWOLUTKU"),
    (2, "KRAJOZNAWCZO"),
    (3, "NIECO MOCNIEJ"),
    (4, "OGIEN"),
)

SUBJECT = (
    (1, "MOTOCYKLE"),
    (2, "KASKI"),
    (3, "KURTKI"),
    (4, "SPODNIE"),
    (5, "BUTY"),
    (6, "MIEJSCA"),
    (7, "INNE"),
)


class Trip(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="opis wyjazdu")
    topic = models.CharField(max_length=50, verbose_name="tytuł")
    create_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    style = models.IntegerField(choices=STYLE, verbose_name="styl jazdy")
    distans = models.IntegerField(verbose_name="planowany dystans w obie strony")
    city_start = models.CharField(max_length=20, verbose_name="miasto startu")
    data_start = models.DateField(verbose_name="data startu (RRRR-MM-DD)")

    def __str__(self):
        return f"{self.topic} - dystans: {self.distans}"

class CommentTrip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

class Relation(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="co tam sie nie dzialo?")
    topic = models.CharField(max_length=50, verbose_name="gdzie bylismy")
    create_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    style = models.IntegerField(choices=STYLE, verbose_name="styl jazdy")
    distans = models.IntegerField(verbose_name="planowany dystans w obie strony")
    city_start = models.CharField(max_length=20, verbose_name="miasto startu")
    data_start = models.DateField(verbose_name="data startu (RRRR-MM-DD)")

    def __str__(self):
        return f"{self.topic} - dystans: {self.distans}"

class CommentRelation(models.Model):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="co to za produkt")
    topic = models.CharField(max_length=50, verbose_name="tytuł")
    create_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)
    subject = models.IntegerField(choices=SUBJECT, verbose_name="czego dotyczy")
    price = models.IntegerField(verbose_name="ile to kosztuje")


    def __str__(self):
        return f"{self.topic} - cena: {self.price}"

class CommentReviews(models.Model):
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

