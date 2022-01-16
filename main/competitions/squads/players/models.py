from django.db import models
import requests
from .utils import player_defaults,player_history_defaults


class Enums:
    class Captain(models.IntegerChoices):
        CAPTAIN = 2
        VICE = 1
        PLAYER = 0

    class Role(models.IntegerChoices):
        GOALKEEPER = 0
        DEFENDER = 1
        MIDFIELDER = 2
        STRIKER = 3

    class Substitute(models.IntegerChoices):
        SUBSTITUTE = 1
        ON_FIELD = 0

    class Teams(models.IntegerChoices):
        ARSENAL = 3

# need to add enums for teams
# TODO:
#   - Read all Teams in from json and make into model


class Player(models.Model):
    id = models.IntegerField(primary_key = True)
    second_name = models.CharField(max_length = 20)
    first_name = models.CharField(max_length=20)
    chance_of_playing_next_round = models.IntegerField(default=0)
    chance_of_playing_this_round = models.IntegerField(default=0)
    code = models.PositiveBigIntegerField(default=0)
    cost_change_event = models.IntegerField(default=0)
    cost_change_event_fall = models.IntegerField(default=0)
    cost_change_start = models.IntegerField(default=0)
    cost_change_start_fall = models.IntegerField(default=0)
    dreamteam_count = models.IntegerField()
    element_type = models.IntegerField(default=0)
    ep_next = models.CharField(max_length = 5)
    ep_this = models.CharField(max_length = 5)
    event_points = models.IntegerField(default=0)
    form = models.CharField(max_length=5)
    in_dreamteam = models.BooleanField()
    news = models.CharField(max_length=400)
    news_added = models.CharField(max_length=20)
    now_cost = models.IntegerField(default=0)
    photo = models.CharField(max_length=20)
    points_per_game = models.CharField(max_length = 5)
    selected_by_percent = models.CharField(max_length = 5)
    special = models.BooleanField()
    squad_number = models.IntegerField(default=0)
    status = models.CharField(max_length=1)
    # Todo: Change 'team' to Integer Choices
    team = models.IntegerField(default=0)
    team_code = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    transfers_in = models.IntegerField(default=0)
    transfers_in_event = models.IntegerField(default=0)
    transfers_out = models.IntegerField(default=0)
    transfers_out_event = models.IntegerField(default=0)
    value_form = models.CharField(max_length = 5)
    value_season = models.CharField(max_length = 5)
    web_name = models.CharField(max_length=20)
    minutes = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    own_goals = models.IntegerField(default=0)
    penalties_saved = models.IntegerField(default=0)
    penalties_missed = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    bps = models.IntegerField(default=0)
    influence = models.CharField(max_length = 5)
    creativity = models.CharField(max_length = 5)
    threat = models.CharField(max_length = 5)
    ict_index = models.CharField(max_length = 5)
    influence_rank = models.IntegerField(default=0)
    influence_rank_type = models.IntegerField(default=0)
    creativity_rank = models.IntegerField(default=0)
    creativity_rank_type = models.IntegerField(default=0)
    threat_rank = models.IntegerField(default=0)
    threat_rank_type = models.IntegerField(default=0)
    ict_index_rank = models.IntegerField(default=0)
    ict_index_rank_type = models.IntegerField(default=0)
    corners_and_indirect_freekicks_order = models.IntegerField(default=0)
    corners_and_indirect_freekicks_text = models.CharField(max_length=200)
    direct_freekicks_order = models.IntegerField(default=0)
    direct_freekicks_text = models.CharField(max_length=200)
    penalties_order = models.IntegerField(default=0)
    penalties_text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.code}: {self.second_name}, {self.first_name}; {self.team}'

    # Initialise all players and last-season history

    @classmethod
    def create_all_players(cls):
        all_players = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()["elements"]
        for player in all_players:
            pl = {k: v or player_defaults[k] for k,v in player.items()}
            p = cls(**pl)
            #print(pl)
            #print(f"id is : {p.id}")

            histories = requests \
                .get(f"https://fantasy.premierleague.com/api/element-summary/{p.id}/") \
                .json()["history_past"]
            for history in histories:
                #print(f'HISTORY:\n{history}\n')
                hist = {k: v or player_history_defaults[k] for k,v in history.items()}
                #print(hist)
                ph = PlayerHistory(player=p,**hist)
            yield p, ph



class PlayerHistory(models.Model):
    # TODO: check this later
    player = models.ForeignKey(Player, on_delete=models.CASCADE,related_name='histories')
    season_name = models.CharField(max_length=20)
    element_code = models.IntegerField()
    start_cost = models.IntegerField(default=0)
    end_cost = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    own_goals = models.IntegerField(default=0)
    penalties_saved = models.IntegerField(default=0)
    penalties_missed = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    bps = models.IntegerField(default=0)
    influence = models.CharField(max_length=5)
    creativity = models.CharField(max_length=5)
    threat = models.CharField(max_length=5)
    ict_index = models.CharField(max_length=5)
