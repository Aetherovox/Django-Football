from django.shortcuts import get_object_or_404
import requests
from django.views.generic import ListView, DetailView
from django.urls import reverse


from .models import Player, PlayerHistory
# Create your views here.

# TODO:
#   - List of players
#   - When a player is selected it dumps json in a div below it (detail view)
#       - Route the url handling for the detail view to a javascript function
#
#

def create_all():
    for p, ph in Player.create_all_players():
        p.save()
        ph.save()


#create_all()


class PlayerListView(ListView):
    model = Player
    context_object_name= 'players'
    paginate_by = 10
    # send to Player Detail when we click on a player
    def get_absolute_url(self):
        return reverse('player-detail',kwargs={'pk': self.pk})


class PlayerDetailView(DetailView):
    model = Player





"""    def get_absolute_url(self):
        return reverse('playerhistory_detail',kwargs={'player':self.player.id,'pk': self.pk})"""

class PlayerHistoryListView(ListView):
    model = PlayerHistory
    context_object_name = 'history'
    paginate_by = 3
    
    def get_query_set(self):
        element = get_object_or_404(Player,id=self.kwargs.get('code'))
        return PlayerHistory.objects.filter(element_code=element)

"""
    def get_absolute_url(self):
        return reverse('playerhistory_detail',kwargs={'pk': self.pk})"""
"""
    def get_context_data(self, *args, **kwargs):
        context = super(PlayerHistoryListView,self).get_context_data(**kwargs)
        context['player'] = kwargs['player']
        return context
"""


class PlayerHistoryDetailView(DetailView):
    model = PlayerHistory



