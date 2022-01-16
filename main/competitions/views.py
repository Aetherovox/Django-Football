from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model as user_model
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Competition, Participant
from .api import CompetitionSerializer, ParticipantSerializer, LeagueSerializer
from .services import AllLeaguesFetcher
User = user_model()
# Create your views here.


class Competitions(ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class ParticipantsView(ModelViewSet):
    serializer_class = ParticipantSerializer
    # lookup_url_kwarg = 'competition__id'
    #
    # def get_queryset(self):
    #     comp_id = self.kwargs.get(self.lookup_url_kwarg)
    #     return Participant.objects.filter(competition = comp_id)

class LeaguesViews(ModelViewSet):
    serializer_class = LeagueSerializer

    def get_queryset(self):
        all_leagues = AllLeaguesFetcher
        all_leagues_data = all_leagues.get_leagues()
        for league_data in all_leagues_data:
            serializer = LeagueSerializer(**league_data)
            if serializer.is_valid():
                print(f"SAVING LEAGUES {league_data}")
                serializer.save()
            else:
                print(f"SERILIZER INVALID\n{serializer.errors}")




