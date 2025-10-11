from django.shortcuts import render
from rest_framework import viewsets
from .models import Contest, ContestExercise, ContestParticipant, ParticipantAnswer
from .serializers import (
      ContestSerializer,
      ContestExerciseSerializer,
      ContestParticipantSerializer,
      ParticipantAnswerSerializer
)


class ContestViewSet(viewsets.ModelViewSet):
      queryset = Contest.objects.all()
      serializer_class = ContestSerializer


class ContestExerciseViewSet(viewsets.ModelViewSet):
      queryset = ContestExercise.objects.all()
      serializer_class = ContestExerciseSerializer


class ContestParticipantViewSet(viewsets.ModelViewSet):
      queryset = ContestParticipant.objects.all()
      serializer_class = ContestParticipantSerializer


class ParticipantAnswerViewSet(viewsets.ModelViewSet):
      queryset = ParticipantAnswer.objects.all()
      serializer_class = ParticipantAnswerSerializer
