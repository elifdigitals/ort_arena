from rest_framework import serializers
from .models import Contest, ContestExercise, ContestParticipant, ParticipantAnswer


class ContestSerializer(serializers.ModelSerializer):
      class Meta:
            model = Contest
            fields = '__all__'


class ContestExerciseSerializer(serializers.ModelSerializer):
      class Meta:
            model = ContestExercise
            fields = '__all__'


class ContestParticipantSerializer(serializers.ModelSerializer):
      class Meta:
            model = ContestParticipant
            fields = '__all__'


class ParticipantAnswerSerializer(serializers.ModelSerializer):
      class Meta:
            model = ParticipantAnswer
            fields = '__all__'
