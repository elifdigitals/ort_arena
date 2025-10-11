from rest_framework import serializers
from .models import Subject, Topic, Exercise, ExerciseTest


class SubjectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Subject
            fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
      subject_name = serializers.ReadOnlyField(source='subject.subject_name')

      class Meta:
            model = Topic
            fields = '__all__'


class ExerciseTestSerializer(serializers.ModelSerializer):
      class Meta:
            model = ExerciseTest
            fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
      subject_name = serializers.ReadOnlyField(source='subject.subject_name')
      topic_name = serializers.ReadOnlyField(source='topic.topic_name')
      tests = ExerciseTestSerializer(many=True, read_only=True)

      class Meta:
            model = Exercise
            fields = '__all__'
