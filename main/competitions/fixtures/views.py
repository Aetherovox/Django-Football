from django_filters.rest_framework import DjangoFilterBackend
from django.core import exceptions
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet
from .models import Fixture, Team,Prediction
from .api import FixtureSerializer, PredictionSerializer, TeamSerializer
from .services import LeagueData





class FixtureAPIView(ModelViewSet):
    serializer_class = FixtureSerializer

    def get_queryset(self):
        """ Refreshes fixtures for a given league by pulling from the FootballWebPages api (rapidapi.com).
            See ./services.py
            We deserialize the data into the models using our same FixtureSerializer
        """
        print("GET QUERY SET!!!")
        league = self.kwargs['comp']
        source_data = LeagueData(league)
        league_fixtures = source_data.get_league_fixtures()  # returns list of dicts for fixtures
        league_teams = source_data.get_teams()  # returns list of dicts for teams

        for teams_data in league_teams:
            serializer = TeamSerializer(data=teams_data)
            if serializer.is_valid():
                # print(serializer.validated_data)
                print(f"Adding new team: {teams_data}")
                serializer.save()
                print("SERIALIZER SUCCESSFUL")

        for fixtures_data in league_fixtures:
            fixtures_data["league"] = league
            serializer = FixtureSerializer(data=fixtures_data)
            if serializer.is_valid():
                # print(serializer.validated_data)
                serializer.save()
                print("SERIALIZER SUCCESSFUL")

            else:
                print(f"!SERIALIZER NOT VALID!\n{serializer.errors}")

        objects = Fixture.objects.all()
        return objects


