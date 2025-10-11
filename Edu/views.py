from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject, Topic, Exercise, ExerciseTest
from .serializers import SubjectSerializer, TopicSerializer, ExerciseSerializer, ExerciseTestSerializer


class SubjectViewSet(viewsets.ModelViewSet):
      queryset = Subject.objects.all()
      serializer_class = SubjectSerializer


class TopicViewSet(viewsets.ModelViewSet):
      queryset = Topic.objects.all()
      serializer_class = TopicSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
      queryset = Exercise.objects.all()
      serializer_class = ExerciseSerializer


class ExerciseTestViewSet(viewsets.ModelViewSet):
      queryset = ExerciseTest.objects.all()
      serializer_class = ExerciseTestSerializer
