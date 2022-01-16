from django.db import models
from competitions.models import Participant,Competition
from django.contrib.auth import get_user_model as user_model
User = user_model()
# Create your models here.


# need to bring in teams from a different app maybe?


class Fixture(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    league = models.ForeignKey(Competition,on_delete=models.CASCADE,related_name = 'fixtures')
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)
    home_team = models.ForeignKey("TeamScore",
                                       on_delete=models.CASCADE,
                                       related_name="fixtures_home",
                                       default=0)
    away_team = models.ForeignKey("TeamScore",
                                       on_delete=models.CASCADE,
                                       related_name="fixtures_away",
                                       default=999)
    status = models.ForeignKey("MatchStatus",
                               related_name='statuses',
                               on_delete=models.PROTECT,
                               db_column="status_id",
                               default='FT')


class TeamScore(models.Model):
    team = models.ForeignKey("Team",on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    score = models.IntegerField(null=True,blank=True)
    half_time_score = models.IntegerField(null=True,blank=True)


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=200,blank=True,null=True)
    short_name = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return f"{self.short_name}"


class MatchStatus(models.Model):
    short = models.CharField(max_length=5,primary_key=True)
    full = models.CharField(max_length=20)


class Prediction(models.Model):
    participant = models.ForeignKey(Participant,on_delete=models.CASCADE,related_name='predictions',default=0)
    fixture = models.ForeignKey(Fixture, on_delete=models.PROTECT,related_name='predictions',null=True)
    score_a = models.PositiveSmallIntegerField()
    score_h = models.PositiveSmallIntegerField()
    teamwin = models.IntegerField(choices =(('DRAW',0),('HOME',1),('AWAY',2)))


