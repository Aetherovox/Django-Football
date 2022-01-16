from .models import Competition,Participant
from .fixtures.api import FixtureSerializer
from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField,ReadOnlyField,StringRelatedField




class ParticipantSerializer(ModelSerializer):
    user = StringRelatedField(source='user.username')
    competition = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Participant
        fields = '__all__'

    def get_queryset(self):
        return Participant.objects.all().order_by('ranking')


class CompetitionSerializer(ModelSerializer):
    participants = ParticipantSerializer(many=True)
    fixtures = FixtureSerializer(many=True)
    creator = StringRelatedField(source='creator.username')

    class Meta:
        model = Competition
        fields = ['id','title','creator','date_started','participants']

    def get_queryset(self):
        return Competition.objects.all().order_by('-date_started')

    # need to create custom create and update methods since nested serializers are readonly by default

    def create(self,validated_data):
        print(validated_data)
        p_data = validated_data.pop('participants')
        competition = Competition.objects.create(**validated_data)
        for participant_data in p_data:
            Participant.objects.create(competition=competition,**participant_data)
        return competition

    def update(self,instance,validated_data):
        print(instance)
        print(validated_data)
        participants_data = validated_data.pop('participants')
        instance.title = validated_data.get('title',instance.title)
        instance.creator = validated_data.get('creator',instance.creator)
        instance.date_started = validated_data.get('date_started',instance.date_started)

        participants_list = []
        for participant_data in participants_data:
            participant,created = Participant.objects.get_or_create(**participant_data)
            participants_list.append(participant)
            # participant = participants.pop(0)
            # participant.user = participant_data.get('user',participant.user)
            # participant.ranking = participant_data.get('ranking', participant.ranking)
            # participant.score = participant_data.get('score', participant.score)
            # participant.save()
        instance.participants.set(participants_list)
        instance.save()
        return instance
