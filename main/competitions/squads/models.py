from django.db import models
from django.contrib.auth import get_user_model as user_model
# Create your models here.
from .players.models import Player
User = user_model()

class Squad(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    player = models.ManyToManyField(Player, related_name = 'squads')

