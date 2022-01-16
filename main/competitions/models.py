from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model as user_model
User = user_model()


class League(models.Model):
    id = models.IntegerField(primary_key=True)
    generic_name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)


# Create your models here.
class Competition(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    date_started = models.DateTimeField(default=timezone.now)
    league = models.ForeignKey(League,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.date_started}'


class Participant(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField()
    ranking = models.IntegerField()
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE,default=0,related_name='participants')

    def __str__(self):
        return f'{self.user.__str__()}_{self.competition.id}'