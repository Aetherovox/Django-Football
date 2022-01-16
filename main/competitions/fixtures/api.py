from django.shortcuts import get_object_or_404
from .models import Fixture, Prediction, Team, TeamScore, MatchStatus
from competitions.models import Competition
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField,RelatedField


# TODO: need score for a particular fixture
#   - This way we dodge the integrity constraints
#   - home_team should be called home_team_score
#   - need a team score model
class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'short_name', 'full_name',)


class IdRelatedField(RelatedField):
    def to_internal_value(self, data):
        print(data)
        return data

    def to_representation(self, value):
        return value


class TeamScoreSerializer(ModelSerializer):
    id = IdRelatedField(queryset=Team.objects.all())

    class Meta:
        model = TeamScore
        fields = ('id','score','name')


class StatusSerializer(ModelSerializer):
    class Meta:
        model = MatchStatus
        fields = ('short','full',)
        extra_kwargs = {
            'short':{'validators':[]}
        }


class PredictionSerializer(ModelSerializer):
    class Meta:
        model = Prediction
        fields = [field.name for field in model._meta.get_fields()]


class FixtureSerializer(ModelSerializer):
    league = PrimaryKeyRelatedField(queryset=Competition.objects.all(),write_only=True)
    predictions = PredictionSerializer(write_only=True,many=True,required=False)
    home_team = TeamScoreSerializer(many=False,required=False)
    away_team = TeamScoreSerializer(many=False,required=False)
    status = StatusSerializer (many=False,required=False)

    class Meta:
        model = Fixture
        fields = [field.name for field in model._meta.get_fields()]

    def create(self,validated_data):
        print('Creating\n -- {}'.format(validated_data))

        home_scores_data = validated_data.pop('home_team')
        away_scores_data = validated_data.pop('away_team')
        status_data = validated_data.pop('status')
        predictions_data = validated_data.pop('predictions', None)

        home_id = home_scores_data.pop('id')
        away_id = away_scores_data.pop('id')

        home_scores, _ = TeamScore.objects.get_or_create(team_id=home_id, **home_scores_data)
        print(f'home_scores: {home_scores}')
        validated_data['home_team'] = home_scores
        away_scores, _ = TeamScore.objects.get_or_create(team_id=away_id, **away_scores_data)
        validated_data['away_team'] = away_scores

        status, _ = MatchStatus.objects.get_or_create(**status_data)
        validated_data['status'] = status

        print(f"CREATING OBJECTS using data: \n{validated_data}")
        fixture = Fixture.objects.create(**validated_data)
        print("Success")
        if predictions_data is not None:
            for prediction in predictions_data:
                Prediction.objects.create(fixture=fixture,**prediction)

        return fixture

    def update(self,instance,validated_data):
        print('Updating\n{}'.format(validated_data))
        # pop model foreign keys
        comps_data = validated_data.pop('competition')
        home_data = validated_data.pop('home_team')
        away_data = validated_data.pop('away_team')
        status_data = validated_data.pop('status')
        predictions_data = validated_data.pop('predictions', None)

        # save all direct fixture fields
        instance.id = validated_data['id']
        instance.date = validated_data['date']
        instance.venue = validated_data['venue']
        instance.time = validated_data['time']
        instance.date = validated_data['date']
        instance.referee = validated_data['referee']

        model_meta = [{'modelname':Prediction,'instance':instance.prediction,'data':predictions_data},
                     {'modelname': Prediction, 'instance': instance.prediction,'data':comps_data},
                     {'modelname': Team, 'instance': instance.home_team,'data':home_data},
                     {'modelname': Team, 'instance': instance.away_team,'data':away_data},
                     {'modelname': MatchStatus, 'instance': instance.status,'data':status_data}]


        def populate_model(model_hash):
            if model_hash['data'] is None:
                return
            obj_list = []
            for data in model_hash['data']:
                existing, created = model_hash['modelname'].objects.get_or_create(**data)
                obj_list.append(existing)
            model_hash['instance'].set(obj_list)
            return

        for model_hash in model_meta:
            populate_model(model_hash)

        instance.save()


