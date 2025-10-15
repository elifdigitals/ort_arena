from rest_framework import serializers
from .models import Contest, ContestParticipant, ParticipantAnswer, ContestExercise, UserRating
from Edu.models import Exercise, Subject


class SubjectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subject
            fields = ['id', 'subject_name', 'description']


class ExerciseSerializer(serializers.ModelSerializer):
      class Meta:
            model = Exercise
            fields = ['id', 'text', 'type', 'difficulty', 'points']


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
