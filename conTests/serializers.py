from rest_framework import serializers
from .models import Contest, ContestParticipant, ParticipantAnswer, ContestExercise, UserRating, Duel
from Edu.models import Exercise, Subject


class SubjectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subject
            fields = ['id', 'subject_name', 'description']
            ref_name = 'ConTestsSubject'


class ExerciseSerializer(serializers.ModelSerializer):
      class Meta:
            model = Exercise
            fields = ['id', 'text', 'type', 'difficulty', 'points']
            ref_name = 'ConTestsExercise'


class ContestExerciseSerializer(serializers.ModelSerializer):
      exercise = ExerciseSerializer(read_only=True)

      class Meta:
            model = ContestExercise
            fields = ['id', 'exercise']


class ContestSerializer(serializers.ModelSerializer):
      subject = SubjectSerializer(read_only=True)
      exercises = ContestExerciseSerializer(many=True, read_only=True)

      class Meta:
            model = Contest
            fields = [
                  'id', 'name', 'contest_type', 'subject',
                  'start_time', 'end_time', 'duration',
                  'description', 'exercises'
            ]


class ContestParticipantSerializer(serializers.ModelSerializer):
      user = serializers.StringRelatedField(read_only=True)

      class Meta:
            model = ContestParticipant
            fields = ['user', 'score', 'finish_time']


class ParticipantAnswerSerializer(serializers.ModelSerializer):
      class Meta:
            model = ParticipantAnswer
            fields = ['id', 'exercise', 'answer_text', 'is_correct', 'answered_time']


class UserRatingSerializer(serializers.ModelSerializer):
      user = serializers.StringRelatedField(read_only=True)

      class Meta:
            model = UserRating
            fields = ['user', 'rating', 'rank']


class DuelSerializer(serializers.ModelSerializer):
    challenger_name = serializers.CharField(source='challenger.username', read_only=True)
    opponent_name = serializers.CharField(source='opponent.username', read_only=True)
    winner_name = serializers.CharField(source='winner.username', read_only=True)

    class Meta:
        model = Duel
        fields = [
            'id', 'challenger_name', 'opponent_name', 'status',
            'started_at', 'finished_at', 'winner_name'
            ]